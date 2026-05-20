import os

from langchain_community.document_loaders.word_document import \
    UnstructuredWordDocumentLoader

# 需要本机有 libreoffice
loader = UnstructuredWordDocumentLoader(
    file_path=os.path.join(os.path.dirname(__file__), "assets", "sample.doc"),
    mode="single",
    # strategy="fast",
)

data = loader.load()

print(data)
