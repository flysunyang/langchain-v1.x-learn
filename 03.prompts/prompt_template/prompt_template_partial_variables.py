from langchain_core.prompts import PromptTemplate
from datetime import datetime
import time

template = PromptTemplate.from_template(
    template="现在时间是：{time},请对我的问题给出答案，我的问题是：{question}",
    partial_variables={"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
)
prompt1 = template.format(question="今天是几号？")
print(prompt1)

time.sleep(2)  # 程序暂停 2 秒，期间不执行任何代码

template2 = PromptTemplate.from_template(
    "现在时间是：{time},请对我的问题给出答案，我的问题是：{question}"
)
partial = template2.partial(time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
prompt2 = partial.format(question="今天是几号？")
print(prompt2)

template3 = PromptTemplate(
    template="{foo} {bar}",
    input_variables=["foo", "bar"],
    partial_variables={"foo": "goodbye"},  # 预先定义部分变量foo值为goodbye
)

prompt = template3.format(bar="lili")
print(prompt)  # goodbye lili

prompt = template3.format(foo="hello", bar="world")  # hello world
print(prompt)
