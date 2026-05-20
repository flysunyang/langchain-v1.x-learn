from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个资深的Python应用开发工程师,请认真回答我提出的Python相关的问题",
        ),
        MessagesPlaceholder("memory"),
        ("human", "{question}"),
    ]
)

prompt = template.invoke(
    {
        "memory": [
            ("human", "我的名字叫亮仔，是一名程序员111"),
            ("ai", "好的，亮仔你好222"),
        ],
        "question": "请问我的名字叫什么？",
    }
)

print(prompt.to_messages())
print(f"prompt type: {type(prompt.to_messages())}")
