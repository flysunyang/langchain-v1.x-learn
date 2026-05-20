from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)
prompt = template.invoke({"role": "后端", "question": "什么是Django?"})
print(prompt)
print(f"prompt type: {type(prompt)}")

print("\n\n")

print(prompt.to_string())
print(f"prompt type: {type(prompt.to_string())}")

print("\n\n")

print(prompt.to_messages())
print(f"prompt type: {type(prompt.to_messages())}")
