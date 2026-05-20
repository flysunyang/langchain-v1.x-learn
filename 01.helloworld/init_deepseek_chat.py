from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

import os

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

print(f"DEEPSEEK_API_KEY: {DEEPSEEK_API_KEY}")

model = init_chat_model(
    model="deepseek-v4-pro",
    # model_provider="deepseek",
    temperature=0,
    timeout=30,
    max_tokens=1000,
    max_retries=3,
)

response = model.invoke("Hello, World!")
print(response.content)
# print(response)
