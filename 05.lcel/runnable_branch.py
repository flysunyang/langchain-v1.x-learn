import os
from langchain.chat_models import init_chat_model
from pydantic import SecretStr
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv

load_dotenv(override=True)

english_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个英语翻译专家，你叫小英"),
        ("human", "请把下面的中文翻译成英文:{query}"),
    ]
)

japanese_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个日语翻译专家，你叫小日"),
        ("human", "请把下面的中文翻译成日文:{query}"),
    ]
)

russian_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个俄语翻译专家，你叫大鹅"),
        ("human", "请把下面的中文翻译成俄文:{query}"),
    ]
)

llm = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=SecretStr(os.environ["TONGYI_API_KEY"]),
    base_url=os.getenv("TONGYI_API_URL"),
)


def determine_language(input) -> str | None:
    query = input["query"]
    if "日语" in query:
        return "japanese"
    elif "英语" in query:
        return "english"
    elif "俄语" in query:
        return "russian"
    return None


parser = StrOutputParser()

chain = RunnableBranch(
    (
        lambda x: determine_language(x) == "japanese",
        japanese_prompt_template | llm | parser,
    ),
    (
        lambda x: determine_language(x) == "english",
        english_prompt_template | llm | parser,
    ),
    (
        lambda x: determine_language(x) == "russian",
        russian_prompt_template | llm | parser,
    ),
    RunnableLambda(lambda x: {"error": "不支持的语言"}),
)


test_queries = [
    {"query": '请你用俄语翻译这句话:"见到你很高兴"'},
    {"query": '请你用日语翻译这句话:"见到你很高兴"'},
    {"query": '请你用英语翻译这句话:"见到你很高兴"'},
    {"query": '请你用韩语翻译这句话:"见到你很高兴"'},
]

for query in test_queries:
    lang = determine_language(query)
    print(f"输入: {query['query']} 语言: {lang}")

    chat_prompt_template = None
    if lang == "japanese":
        chat_prompt_template = japanese_prompt_template
    elif lang == "english":
        chat_prompt_template = english_prompt_template
    elif lang == "russian":
        chat_prompt_template = russian_prompt_template

    if chat_prompt_template is None:
        print("不支持的语言，跳过此查询。")
        continue

    prompt = chat_prompt_template.format_messages(**query)
    print(f"生成的提示词: {prompt}\n")
    response = llm.invoke(prompt)
    print(f"输出: {response.content}\n")
