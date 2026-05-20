from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from pydantic import SecretStr
from langchain_core.output_parsers import JsonOutputParser
import json

load_dotenv(override=True)

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个{role}，请简短回答我提出的问题，结果返回json格式，q表示字段，a表示答案",
        ),
        ("user", "{question}"),
    ]
)

prompt = prompt_template.invoke(
    {"role": "AI助手", "question": "什么是LangChain，简介回答100字以内"}
)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

response = llm.invoke(prompt)
print(response.content)

print("=== 解析 JSON ===")
json_parser = JsonOutputParser()
parsed = json_parser.invoke(response)
print(f"解析后的结果:\n{json.dumps(parsed, ensure_ascii=False, indent=2)}")
