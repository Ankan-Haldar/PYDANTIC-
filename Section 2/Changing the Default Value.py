from pydantic import BaseModel


class User(BaseModel):
    name: str
    country: str = "India"


user = User(
    name="John",
    country="USA"
)

print(user)


# A default value is used only when the field is omitted. If a valid value is explicitly provided, that value is used.