import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

input_text = "疯狂星期四"

client = OpenAI(
    api_key=os.environ["TONGYI_API_KEY"],
    base_url=os.environ["TONGYI_API_URL"],
)

completion = client.embeddings.create(
    model="text-embedding-v4",
    input=input_text
)
print(completion.model_dump_json())
