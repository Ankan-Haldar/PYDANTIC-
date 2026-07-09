from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str


user = User(
    username="rahul123",
    email="rahul@example.com",
    password="secret123"
)


data = user.model_dump(
    exclude={"password"}
)

print(data)



# The password field is excluded from the serialized output. This is useful when returning public user data.