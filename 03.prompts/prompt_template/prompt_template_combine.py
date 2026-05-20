from langchain_core.prompts import PromptTemplate

template1 = PromptTemplate.from_template(
    "请用一句话介绍{topic}，要求通俗易懂\n" + "内容不超过{length}个字"
)

prompt = template1.format(topic="LangChain", length=100)
print(prompt)

prompt_a = PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂\n")
prompt_b = PromptTemplate.from_template("内容不超过{length}个字")
prompt_all = prompt_a + prompt_b
prompt2 = prompt_all.format(topic="LangChain", length=200)
print(prompt2)
