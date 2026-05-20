import os

from langchain_community.document_loaders.pdf import PyPDFLoader

loader = PyPDFLoader(
    file_path=os.path.join(os.path.dirname(__file__), "assets", "sample.pdf"),
    mode="single",
    pages_delimiter="\n\f",
)

data = loader.load()

print(data)
