from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        str_to_lower=True
    )

    username: str
    city: str


user = User(
    username="ANKAN123",
    city="KOLKATA"
)


print(user)


# All string fields are automatically converted to lowercase.