from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate(
    [
        ("system", "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")
    ]
)
prompt = template.format(role="后端", question="什么是Django?")
print(prompt)
print(f"prompt type: {type(prompt)}")

print("\n\n")

chatPromptTemplate = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)
prompt = chatPromptTemplate.format_messages(
    name="小明",
    thing="有用的工具",
    user_input="你能帮我开发一个什么样的工具?"
)
print(prompt)
print(f"prompt type: {type(prompt)}")
