from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20
    )


user = User(
    username="AI"
)

# "AI" contains only 2 characters, but the minimum required length is 3.