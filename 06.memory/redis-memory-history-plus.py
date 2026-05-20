import os

from dotenv import load_dotenv
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig, RunnableWithMessageHistory
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

template = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder("history"), ("human", "{question}")]
)

REDIS_URL = "redis://localhost:6379"


def get_by_session_id(session_id: str) -> RedisChatMessageHistory:
    history = RedisChatMessageHistory(session_id=session_id, url=REDIS_URL)
    return history


chain_with_history = RunnableWithMessageHistory(
    template | llm,
    get_by_session_id,
    input_messages_key="question",
    history_messages_key="history",
)


print("开始对话（输入 'quit' 退出）")
while True:
    question = input("\n输入问题：")
    if question.lower() in ["quit", "exit", "q"]:
        break

    config = RunnableConfig({"configurable": {"session_id": "user_bob"}})
    response = chain_with_history.invoke({"question": question}, config)
    logger.info(f"AI回答:{response.content}")
