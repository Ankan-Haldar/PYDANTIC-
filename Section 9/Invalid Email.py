from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr


user = User(
    email="rahul-invalid-email"
)

# The value does not follow a valid email format, so Pydantic rejects it.