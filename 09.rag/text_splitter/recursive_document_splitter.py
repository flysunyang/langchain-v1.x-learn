import os

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 直接读取文本文件，避免依赖 spaCy
file_path = os.path.join(os.path.dirname(__file__), "note.txt")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

documents = [Document(page_content=content, metadata={"source": file_path})]
print(documents)
print(type(documents))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)

splitter_documents = text_splitter.split_documents(documents)

print(f"分割文档数量：{len(splitter_documents)}")

for splitter_document in splitter_documents:
    print(f"文档片段：{splitter_document.page_content}")
    print(
        f"文档片段大小：{len(splitter_document.page_content)}, \
            文档元数据：{splitter_document.metadata}"
    )
