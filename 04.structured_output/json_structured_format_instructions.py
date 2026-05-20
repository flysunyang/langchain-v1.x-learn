import json
import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field, SecretStr
from langchain_core.output_parsers import JsonOutputParser

load_dotenv(override=True)


class NewsFormatInstructions(BaseModel):
    time: str = Field(description="新闻发布时间")
    person: str = Field(description="新闻发布人")
    event: str = Field(description="新闻事件描述")


# pydantic_object 定义输出的结构
parser = JsonOutputParser(pydantic_object=NewsFormatInstructions)
# get_format_instructions 获取格式指令模板
format_instructions_template = parser.get_format_instructions()
print(format_instructions_template)


prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个AI助手，你只能输出结构化JSON数据",
        ),
        ("human", "请生成一个关于{topic}的新闻。{format_instructions}"),
    ]
)

prompt = prompt_template.format_messages(
    topic="小米su7跑车", format_instructions=format_instructions_template
)
print(prompt)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

response = llm.invoke(prompt)
print("=== LLM 输出 ===")
print(response.content)
print(type(response.content))

# JsonOutputParser 解析输出返回的是 Dictionary
parsed = parser.invoke(response)
print("=== 解析后的结果 ===")
print(json.dumps(parsed, ensure_ascii=False, indent=2))
print(type(parsed))
