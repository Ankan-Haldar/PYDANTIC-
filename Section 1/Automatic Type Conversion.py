from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


user = User(
    name="Rahul",
    age="25"
)

print(user)
print(type(user.age))


# The input value "25" is a string, but the model expects an integer. Pydantic converts the compatible string value into the integer 25.