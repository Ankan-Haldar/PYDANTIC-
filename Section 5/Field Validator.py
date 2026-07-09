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
    username="ankan123"
)

print(user)



# The validator checks only the username field. Since the username contains no spaces, validation succeeds.