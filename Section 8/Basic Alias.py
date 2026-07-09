from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        alias="userName"
    )

    age: int


user = User(
    userName="Rahul123",
    age=23
)

print(user)

# The external input uses userName, but inside Python the field is accessed as username.