import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import SecretStr
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv(override=True)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role}，请简短的回答我提出的问题"),
        ("human", "请回答：{question}"),
    ]
)

prompt = prompt_template.format_messages(
    role="AI助手", question="什么是LangChain，简介回答100字以内"
)
# print(prompt)


llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

response = llm.invoke(prompt)
print(response.content)

parser = StrOutputParser()
parsed = parser.invoke(response)
print("=== 解析后的结果 ===")
print(parsed)
print(type(parsed))
