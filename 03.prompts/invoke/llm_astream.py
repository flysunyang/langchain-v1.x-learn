import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv(override=True)


llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=os.environ["TONGYI_API_KEY"],
    base_url=os.getenv("TONGYI_API_URL"),
)


async def main():
    response = llm.astream("你是谁?")
    async for chunk in response:
        print(chunk.content, end="", flush=True)
    print("\n")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
