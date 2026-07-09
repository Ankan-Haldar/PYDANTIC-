from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        alias="userName"
    )


user = User(
    userName="Ankan123"
)


print(user.username)



# The alias is used for input, but the Python model attribute remains username.