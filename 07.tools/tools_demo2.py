from langchain.tools import tool
from pydantic import BaseModel, Field


class FieldInfo(BaseModel):
    """
    定义加法运算所需的输入参数结构
    """

    a: int = Field(description="第一个加数")
    b: int = Field(description="第二个加数")


@tool(args_schema=FieldInfo)
def add_number(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


result = add_number.invoke({"a": 1, "b": 2})
print(result)

print()

print(f"{add_number.name=}\n{add_number.description=}\n{add_number.args=}\n")
print(f"{add_number.args_schema=}\n{add_number.return_direct}")
