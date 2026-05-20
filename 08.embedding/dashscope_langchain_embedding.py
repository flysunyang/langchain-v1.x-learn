import os

from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings

load_dotenv(override=True)

embeddings = DashScopeEmbeddings(
    model="text-embedding-v1",
    dashscope_api_key=os.environ["TONGYI_API_KEY"]
)

text = "This is a test document."

# embed_query 用于将查询文本转换为向量
query_result = embeddings.embed_query(text)
print(query_result)

# embed_documents 用于将文本列表转换为向量列表
doc_result = embeddings.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
print(doc_result)
# sep=' 用于分隔输出，避免换行
# 文本向量数量：5, 文本向量长度：1536
print(f"文本向量数量:{len(doc_result)}, 文本向量长度:{len(doc_result[0])}", sep='')
