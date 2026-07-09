from pydantic import BaseModel


class User(BaseModel):
    name: str
    phone: str | None = None


user = User(
    name="Rahul"
)

print(user)


# The phone field can contain a string or None. Since its default is None, the field can also be omitted.