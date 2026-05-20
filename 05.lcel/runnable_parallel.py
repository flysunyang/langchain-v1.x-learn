import os
from langchain.chat_models import init_chat_model
from pydantic import SecretStr
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv(override=True)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

joke_chain = (
    ChatPromptTemplate.from_template("tell me a joke about {topic}") | llm
)

poem_chain = (
    ChatPromptTemplate.from_template("write a 2-line poem about {topic}") | llm
)

runnable = RunnableParallel(joke=joke_chain, poem=poem_chain)

response = runnable.invoke({"topic": "cats"})
print(response)

runnable.get_graph().print_ascii()
