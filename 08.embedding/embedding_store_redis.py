import os

from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.documents import Document
from langchain_redis import RedisVectorStore

load_dotenv(override=True)

# 初始化 Embedding 模型
embeddings = DashScopeEmbeddings(
    model="text-embedding-v1", dashscope_api_key=os.environ["TONGYI_API_KEY"]
)

# 初始化 Redis Vector Store
vector_store = RedisVectorStore(
    # redis index prefix
    index_name="langchain-demo-index",
    embeddings=embeddings,
    redis_url="redis://localhost:6379",
)

# 准备文档
documents = [
    Document(
        page_content="LangChain is a framework for building LLM applications.",
        metadata={"source": "langchain"},
    ),
    Document(
        page_content="Redis supports vector similarity search.",
        metadata={"source": "redis"},
    ),
    Document(
        page_content="OpenAI provides embedding models.",
        # metadata 表示文档的来源，这里是一个字符串，有多个来源
        metadata={"source": "openai"},
    ),
]

ids = vector_store.add_documents(documents)
print("写入成功, ids:", ids)

# 相似度搜索
# results = vector_store.similarity_search(
#     query="What database support vector search?", k=2
# )

# print("\n搜索结果：\n")

# for doc in results:
#     print(doc.page_content)
#     print(doc.metadata)


# 带得分的 score
results = vector_store.similarity_search_with_score(
    query="What database support vector search?", k=2
)

for doc, score in results:
    print(f"* [SIM={score:.3f}] {doc.page_content} [{doc.metadata}]")
