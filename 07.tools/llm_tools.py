import os

from dotenv import load_dotenv
from get_weather import get_weather_by_city
from langchain_core.output_parsers import JsonOutputKeyToolsParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import SecretStr

from langchain.chat_models import init_chat_model

load_dotenv(override=True)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)

llm_bind_tools = llm.bind_tools([get_weather_by_city])

parser = JsonOutputKeyToolsParser(
    key_name=get_weather_by_city.name, first_tool_only=True
)

get_weather_chain = llm_bind_tools | parser | get_weather_by_city

# response = get_weather_chain.invoke("合肥的天气怎么样")
# print(response)

output_prompt = ChatPromptTemplate.from_template(
    """你将收到一段 JSON 格式的天气数据{weather_json}，请用简洁自然的方式将其转述给用户。
    以下是天气 JSON 数据：
    请将其转换为中文天气描述，例如：
    “北京现在天气：多云，气温 28℃，体感有点闷热（约 32℃），湿度 75%，微风（东南风 2 米/秒），
    能见度很好，大约 10 公里。建议穿短袖短裤。适合做户外运动。"
    """
)

full_chain = get_weather_chain | \
    (lambda x: {"weather_json": x}) | output_prompt | llm

response = full_chain.invoke("合肥的天气怎么样")
print(response)
