from langchain.tools import tool


@tool
def add_number(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


result = add_number.invoke({"a": 1, "b": 2})
print(result)

print()

print(f"{add_number.name=}\n{add_number.description=}\n{add_number.args=}")
