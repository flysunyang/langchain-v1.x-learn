import os

import dashscope
from dotenv import load_dotenv

load_dotenv(override=True)

text = "这是一段测试文本，用于生成多模态融合向量"
image = "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"

input_data = [
    {"text": text},
    {"image": image},
]

resp = dashscope.MultiModalEmbedding.call(
    api_key=os.environ["TONGYI_API_KEY"],
    model="qwen3-vl-embedding",
    input=input_data,
    enable_fusion=True,
    dimension=1024,
)

print(resp.output)
