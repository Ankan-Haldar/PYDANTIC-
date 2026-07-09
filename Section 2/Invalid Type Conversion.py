from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int


employee = Employee(
    name="Amit",
    age="hello"
)



# Pydantic cannot convert "hello" into an integer, so model creation fails.