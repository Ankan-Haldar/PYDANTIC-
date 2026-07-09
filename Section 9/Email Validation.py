# pip install email-validator------> First



from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr


user = User(
    name="Rahul",
    email="rahul@example.com"
)

print(user)

# EmailStr checks whether the input follows a valid email format.