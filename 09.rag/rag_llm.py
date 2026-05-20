import os

from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_redis import RedisVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_unstructured import UnstructuredLoader
from pydantic import SecretStr

from langchain.chat_models import init_chat_model

load_dotenv(override=True)

# index
# 1.创建向量模型
embeddings = DashScopeEmbeddings(
    model="text-embedding-v1", dashscope_api_key=os.environ["TONGYI_API_KEY"]
)

# 2.创建向量数据库
vector_store = RedisVectorStore(
    # redis index prefix
    index_name="langchain-rag",
    embeddings=embeddings,
    redis_url="redis://localhost:6379",
)

# 3.读取 docx 文本内容
file_path = os.path.join(os.path.dirname(__file__), "alibaba-java.docx")
loader = UnstructuredLoader(file_path)
documents = loader.load()

# 4.分词
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)
splitter_documents = text_splitter.split_documents(documents)

# 5.向量化，存入 redis
vector_store.add_documents(splitter_documents)

# retrieval
# 6.检索，获取 top_k
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 7.创建 chain
prompt_template = """
    请使用以下提供的文本内容来回答问题。仅使用提供的文本信息，
    如果文本中没有相关信息，请回答"抱歉，提供的文本中没有这个信息"。

    文本内容：
    {context}

    问题：{question}

    回答：
    "
"""

prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

rag_chain = {"context": retriever, "question": RunnablePassthrough()} \
    | prompt | llm

# 测试
question = "00000和A0001分别是什么意思"
result = rag_chain.invoke(question)
print("\n问题:", question)
print("\n回答:", result.content)
