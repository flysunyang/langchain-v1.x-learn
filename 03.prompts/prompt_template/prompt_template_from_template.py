from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    template="你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)
prompt = template.format(role="Java", question="什么是Spring?")
print(prompt)
print(f"prompt type: {type(prompt)}")


print("\n\n")


template = PromptTemplate.from_template("请给我一个关于{topic}的{type}解释。")
prompt = template.format(topic="人工智能", type="简要")
print(prompt)
