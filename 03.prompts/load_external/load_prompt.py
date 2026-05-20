from langchain_core.load import loads
from pathlib import Path

prompt_file = Path(__file__).parent / "my_prompt.json"

# 从文件读取 JSON
with open(prompt_file, "r") as f:
    json_str = f.read()

# 反序列化（如果需要注入密钥，添加 secrets_map）
prompt = loads(json_str)

# 使用加载的 Prompt
formatted = prompt.format(language="Chinese", input="Hello!")
print(formatted)
# 输出: System: You are a helpful assistant that speaks Chinese.
#       Human: Hello!
