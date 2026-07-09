from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        extra="allow"
    )

    name: str
    age: int


user = User(
    name="Rahul",
    age=23,
    city="Kolkata"
)

print(user)
print(user.city)


# With extra="allow", additional fields are accepted and available on the model.