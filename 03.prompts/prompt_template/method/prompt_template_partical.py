from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)
# prompt = template.format(**{"role": "后端", "question": "什么是Django?"})
partial_template = template.partial(role="后端")
print(partial_template)
print(f"partial_template type: {type(partial_template)}")
print("\n\n")

prompt = partial_template.format(question="什么是Django?")
print(prompt)
print(f"prompt type: {type(prompt)}")
