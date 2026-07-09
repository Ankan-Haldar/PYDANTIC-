from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str

    @field_validator("name", mode="before")
    @classmethod
    def clean_name(cls, value):
        return value.strip()


user = User(
    name="   Rahul   "
)

print(user.name)


# The validator runs before normal validation and removes extra spaces from the raw input.