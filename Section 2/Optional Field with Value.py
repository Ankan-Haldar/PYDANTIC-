from pydantic import BaseModel


class User(BaseModel):
    name: str
    phone: str | None = None


user = User(
    name="Rahul",
    phone="9876543210"
)

print(user)


# The field accepts either a string value or None. Here, a valid string value was provided.