from typing import Annotated

from pydantic import Field, BaseModel, ValidationError

Age = Annotated[int, Field(ge=0, le=150, description="年龄，必须在0到150之间")]


class Person(BaseModel):
    name: str = Field(description="姓名")
    age: int
    age2: Age


try:
    # person = Person(name="Alice", age=30, age2=200)
    person = Person(name="Bob", age=28, age2=100)
    print(person)
except ValidationError as e:
    print("验证错误:", e)
