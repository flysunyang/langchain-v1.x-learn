from typing import Annotated, TypedDict

Age = Annotated[int, "年龄"]


# TypedDict 定义输出的结构，与 pydantic 模型不同，TypedDict 不会自动添加字段描述
class Person(TypedDict):
    name: str
    age: Age


# PylancereportArgumentTypesMismatch:
# Expected type 'int' (matched generic type 'Annotated[int, str]'),
# got 'str' instead
# p = Person(name="z3", age="1111")
# print(p)

person = Person(name="Alice", age=30)
print(person)
print(type(person))
