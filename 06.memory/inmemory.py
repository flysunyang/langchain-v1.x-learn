import os

from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from loguru import logger
from pydantic import SecretStr

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

load_dotenv(override=True)


llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

history = InMemoryChatMessageHistory()
history.add_message(HumanMessage(content="我叫张三，我的爱好是学习"))

ai_msg = llm.invoke(history.messages)
logger.info(f"AI Message: {ai_msg}")

history.add_message(ai_msg)
history.add_user_message("我叫什么？我的爱好是什么？")

ai_msg = llm.invoke(history.messages)
logger.info(f"AI Message: {ai_msg}")

history.add_message(ai_msg)

print("\nFull chat history:")
for message in history.messages:
    logger.info(f"Message: {message}")
