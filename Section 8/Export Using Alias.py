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


data = user.model_dump(
    by_alias=True
)

print(data)


# by_alias=True uses the alias name in the serialized output.