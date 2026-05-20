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
    questions = ["你是谁?", "今天天气怎么样?"]
    responses = await llm.abatch(inputs=questions)
    for question, response in zip(questions, responses):
        print(f"问题：{question}")
        print(f"回答：{response.content}\n")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
