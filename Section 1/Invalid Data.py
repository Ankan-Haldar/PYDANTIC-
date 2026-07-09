from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


user = User(
    name="Rahul",
    age="hello"
)

# A ValidationError is raised because "hello" cannot be converted into an integer.