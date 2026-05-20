import os
from typing import Annotated, TypedDict
from langchain.chat_models import init_chat_model
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv(override=True)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)


class Animal(TypedDict):
    animal: Annotated[str, "动物"]
    emoji: Annotated[str, "动物表情"]


class AnimalList(TypedDict):
    animals: Annotated[list[Animal], "动物列表"]


llm_with_structured_output = llm.with_structured_output(AnimalList)
response = llm_with_structured_output.invoke(
    [("user", "请以JSON格式输出任意三个动物，以及它们的 emoji 表情")]
)
print(response)
