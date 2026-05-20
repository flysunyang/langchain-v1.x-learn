from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv(override=True)


llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=os.environ["TONGYI_API_KEY"],
    base_url=os.getenv("TONGYI_API_URL")
)

response = llm.invoke("你是谁?")
print(response.content)
