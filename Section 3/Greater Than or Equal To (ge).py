from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(ge=18)


user = User(
    name="Rahul",
    age=18
)

print(user)