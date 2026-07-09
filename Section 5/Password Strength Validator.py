from pydantic import BaseModel, field_validator


class Account(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError(
                "Password must contain at least 8 characters"
            )

        return value


account = Account(
    password="python123"
)

print(account)



# The custom validator checks the password length before accepting the value.