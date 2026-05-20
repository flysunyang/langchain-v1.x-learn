import os
from langchain.chat_models import init_chat_model
from pydantic import SecretStr
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv(override=True)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role},请简短的回答我提出的问题。"),
        ("human", "请回答:{question}"),
    ]
)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

parser = StrOutputParser()

chain = prompt_template | llm | parser

response = chain.invoke({"role": "AI助手", "question": "langgraph是什么?"})
print(response)
print(type(response))
