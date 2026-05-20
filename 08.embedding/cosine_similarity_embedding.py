import os

import numpy as np
from dashscope import TextEmbedding
from dotenv import load_dotenv

load_dotenv(override=True)


def cosine_similarity(a, b):
    """计算余弦相似度"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def semantic_search(query, documents, top_k=5):
    """语义搜索"""
    # 生成查询向量
    query_resp = TextEmbedding.call(
        model="text-embedding-v4",
        input=query,
        dimension=1024,
        api_key=os.environ["TONGYI_API_KEY"],
    )
    query_embedding = query_resp.output["embeddings"][0]["embedding"]

    # 生成文档向量
    doc_resp = TextEmbedding.call(
        model="text-embedding-v4",
        input=documents,
        dimension=1024,
        api_key=os.environ["TONGYI_API_KEY"],
    )

    # 计算相似度
    similarities = []
    print(doc_resp.output["embeddings"])
    for i, doc_emb in enumerate(doc_resp.output["embeddings"]):
        similarity = cosine_similarity(query_embedding, doc_emb["embedding"])
        similarities.append((i, similarity))

    # 排序并返回top_k结果
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [(documents[i], sim) for i, sim in similarities[:top_k]]


if __name__ == "__main__":
    documents = [
        "人工智能是计算机科学的一个分支",
        "机器学习是实现人工智能的重要方法",
        "深度学习是机器学习的一个子领域",
    ]
    query = "什么是AI？"
    results = semantic_search(query, documents, top_k=5)
    for doc, sim in results:
        print(f"相似度: {sim:.3f}, 文档: {doc}")
