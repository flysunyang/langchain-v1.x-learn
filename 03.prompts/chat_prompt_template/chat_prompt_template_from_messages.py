from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    messages=[
        ("system", "你是一个{role}，请回答我提出的问题"),
        ("human", "请回答:{question}"),
    ]
)
prompt_value = template.format_messages(**{"role": "python开发工程师",
                                           "question": "堆排序怎么写"})
print(prompt_value)
print(f"prompt_value type: {type(prompt_value)}")

print("\n\n")

prompt = template.invoke({"role": "python开发工程师", "question": "堆排序怎么写"})
print(prompt.to_string)
print(f"prompt type: {type(prompt.to_string)}")

print("\n\n")

prompt = template.format(role="python开发工程师", question="快速排序怎么写")
print(prompt)
print(f"prompt type: {type(prompt)}")
