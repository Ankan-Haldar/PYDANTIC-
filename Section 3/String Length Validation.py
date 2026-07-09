from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20
    )


user = User(
    username="ankan123"
)

print(user)

# The username contains between 3 and 20 characters, so it passes validation.