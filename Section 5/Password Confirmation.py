from pydantic import BaseModel, model_validator


class RegisterUser(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )

        return self


user = RegisterUser(
    password="python123",
    confirm_password="python123"
)

print(user)

# A model validator is appropriate because the rule requires comparing two fields.