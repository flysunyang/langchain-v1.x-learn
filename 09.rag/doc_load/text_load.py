import os

from langchain_community.document_loaders.text import TextLoader

loader = TextLoader(
    file_path=os.path.join(os.path.dirname(__file__), "assets", "sample.txt"),
    encoding="utf_8"
)

data = loader.load()

print(data)
