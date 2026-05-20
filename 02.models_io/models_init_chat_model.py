from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv(override=True)

llm = init_chat_model(
    model="qwen3.6-plus",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_API_URL")
)

response = llm.invoke([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁?"}
])
print(response.content)
