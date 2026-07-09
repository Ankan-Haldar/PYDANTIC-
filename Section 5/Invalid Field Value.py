from pydantic import BaseModel, field_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if " " in value:
            raise ValueError("Username cannot contain spaces")

        return value


user = User(
    username="ankan haldar"
)

# The custom validator raises ValueError, so Pydantic reports a validation error.