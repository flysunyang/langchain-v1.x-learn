import os
from http import HTTPStatus

import dashscope
from dotenv import load_dotenv

load_dotenv(override=True)

resp = dashscope.TextEmbedding.call(
    model="text-embedding-v3",
    input="衣服的质量杠杠的，很漂亮，喜欢，以后还来这里买",
    api_key=os.environ["TONGYI_API_KEY"],
)

print(resp) if resp.status_code == HTTPStatus.OK else print(resp)
print(f"向量大小：{len(resp.output["embeddings"][0]["embedding"])}")
