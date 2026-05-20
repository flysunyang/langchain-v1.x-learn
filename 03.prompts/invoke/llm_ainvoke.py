from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv(override=True)


def init_llm():
    llm = init_chat_model(
        model="qwen3.6-plus",
        model_provider="openai",
        api_key=os.environ["TONGYI_API_KEY"],
        base_url=os.getenv("TONGYI_API_URL"),
    )
    return llm


async def main():
    llm = init_llm()
    response = await llm.ainvoke("你是谁?")
    print(f"响应类型：{type(response)}")
    print(response.content_blocks)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
