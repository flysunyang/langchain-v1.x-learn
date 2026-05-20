import os
from langchain_deepseek import ChatDeepSeek
from pydantic import SecretStr

llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=SecretStr(os.environ["DEEPSEEK_API_KEY"]),
    # base_url=os.getenv("TONGYI_API_URL"),
)

ai_msgs = llm.invoke(
    [
        ("system", "You are a helpful assistant."),
        ("user", "I like programming")
    ]
)
print(ai_msgs)
