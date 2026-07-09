from pydantic import BaseModel, Field


class Account(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"
    )

    age: int = Field(
        ge=18,
        le=100
    )


account = Account(
    username="ankan_123",
    age=23
)

print(account)


# The username satisfies the length and pattern rules, while the age satisfies the numeric range.