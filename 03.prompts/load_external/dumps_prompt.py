from pathlib import Path
from langchain_core.load import dumps
from langchain_core.prompts import ChatPromptTemplate

# 获取当前脚本所在目录
current_dir = Path(__file__).parent

# 创建 Prompt 对象
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that speaks {language}."),
        ("user", "{input}"),
    ]
)

# 序列化为 JSON 字符串
json_str = dumps(prompt, pretty=True)

# 保存到脚本同目录
output_file = current_dir / "my_prompt.json"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(json_str)

print(f"Prompt saved to: {output_file}")
