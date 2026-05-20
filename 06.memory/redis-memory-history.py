import os

from dotenv import load_dotenv
from langchain_community.chat_message_histories import RedisChatMessageHistory
from loguru import logger
from pydantic import SecretStr

from langchain.chat_models import init_chat_model

load_dotenv(override=True)


llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

REDIS_URL = "redis://localhost:6379"
# redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

history = RedisChatMessageHistory(session_id="user_alice", url=REDIS_URL)
history.add_user_message("Hello, AI assistant! My name is Alice.")
history.add_ai_message("Hello! How can I assist you today?")

response = llm.invoke(history.messages)
logger.info(f"AI Response: {response}")

history.add_ai_message(response)
history.add_user_message("What is my name?")
response = llm.invoke(history.messages)
logger.info(f"AI Response: {response}")
history.add_ai_message(response)

print("\nFull chat history:")
for message in history.messages:
    logger.info(f"Message: {message}")
