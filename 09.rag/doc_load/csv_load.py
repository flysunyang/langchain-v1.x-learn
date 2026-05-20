import os

from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(
    file_path=os.path.join(os.path.dirname(__file__), "assets", "sample.csv"),
)

data = loader.load()

print(data)
