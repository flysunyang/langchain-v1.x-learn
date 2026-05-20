from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="",
    temperature=0
)

ai_msg = llm.invoke([
    ("system", "You are a helpful assistant."),
    ("human", "你是谁？")
])
print(ai_msg)
