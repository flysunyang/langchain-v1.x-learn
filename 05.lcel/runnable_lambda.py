import os
from langchain.chat_models import init_chat_model
from pydantic import SecretStr
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("human", "直接回复：随机给我一个英文人名"),
    ]
)


def add_one(x: int) -> int:
    print(f"Adding one to {x}")
    return x + 1


def say_hello(message) -> str:
    return f"Hello, {message.content}!"


runnable = RunnableLambda(add_one)

response = runnable.invoke(1)
print(response)
response = runnable.batch([1, 2, 3])
print(response)

chain = prompt_template | llm | RunnableLambda(say_hello)
response = chain.invoke({})
print(response)
print(type(response))
