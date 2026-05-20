import os

from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
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
    [(MessagesPlaceholder("history")), ("human", "{question}")]
)


store = {}


def get_session_history(session_id: str):
    """
    根据 session_id 获取对应的历史消息对象。
    如果不存在则创建一个新的 InMemoryChatMessageHistory。
    """
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chain = RunnableWithMessageHistory(
    template | llm,
    get_session_history=get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

config = RunnableConfig(configurable={"session_id": "user_alice"})

logger.info(chain.invoke({"question": "我叫张三，我爱好学习。"}, config))
logger.info(chain.invoke({"question": "我叫什么？我的爱好是什么？"}, config))
