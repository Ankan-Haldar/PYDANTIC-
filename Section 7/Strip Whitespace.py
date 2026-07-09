from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    name: str
    city: str


user = User(
    name="   Rahul   ",
    city="   Kolkata   "
)


print(user.name)
print(user.city)


# Leading and trailing whitespace is automatically removed from string fields.