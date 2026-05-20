import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, SecretStr
from dotenv import load_dotenv

load_dotenv(override=True)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)


class Product(BaseModel):
    """
    产品信息模型类，用于定义产品的结构化数据格式

    属性:
        name (str): 产品名称
        category (str): 产品类别
        description (str): 产品简介，长度必须大于等于10个字符
    """

    name: str = Field(description="产品名称")
    category: str = Field(description="产品类别")
    description: str = Field(description="产品描述")


template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手，你只能输出结构化的json数据\n{format_instructions}"),
        ("human", "请你输出标题为：{topic}的新闻内容"),
    ]
)
parser = PydanticOutputParser(pydantic_object=Product)
prompt = template.format_prompt(
    topic="华为Mate X7", format_instructions=parser.get_format_instructions()
)


llm_with_structured_output = llm.with_structured_output(Product)
response = llm_with_structured_output.invoke(prompt)
print(response)
