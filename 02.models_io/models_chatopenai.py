from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv(override=True)

llm = ChatOpenAI(
    model="qwen3.6-plus",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

messages = [("system", "You are a helpful assistant."), ("user", "你是谁?")]

ai_msg = llm.invoke(messages)
print(ai_msg.content)
