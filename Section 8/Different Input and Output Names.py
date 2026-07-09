from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        validation_alias="user_name",
        serialization_alias="userName"
    )


user = User(
    user_name="ankan123"
)


print(user.username)

print(
    user.model_dump(
        by_alias=True
    )
)


# Input uses user_name, Python uses username, and serialized output uses userName.