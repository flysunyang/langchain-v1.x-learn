from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

client = OpenAI(
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_API_URL")
)

print(f"base_url:{os.getenv("TONGYI_API_URL")}, \
      api_key:{os.getenv("TONGYI_API_KEY")}")

completion = client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁?"}
    ]
)
print(completion.model_dump_json())
