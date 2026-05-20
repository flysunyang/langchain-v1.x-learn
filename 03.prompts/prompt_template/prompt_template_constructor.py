from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}",
    input_variables=["role", "question"],
)
prompt = template.format(role="前端", question="什么是React?")
print(
    prompt
)  # 你是一个专业的前端工程师，请回答我的问题给出回答，我的问题是：什么是React?
print(f"prompt type: {type(prompt)}")  # prompt type: <class 'str'>

print("\n\n")

template = PromptTemplate(
    template="请评价{product}的优缺点，包括{aspect1}和{aspect2}。",
    input_variables=["product", "aspect1", "aspect2"],
)

prompt_1 = template.format(product="iPhone", aspect1="电池续航", aspect2="拍照效果")
prompt_2 = template.format(product="MacBook", aspect1="性能", aspect2="便携性")

print(prompt_1)  # 请评价iPhone的优缺点，包括电池续航和拍照效果。
print(prompt_2)  # 请评价MacBook的优缺点，包括性能和便携性。
