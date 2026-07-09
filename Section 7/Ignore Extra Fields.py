from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        extra="ignore"
    )

    name: str
    age: int


user = User(
    name="Rahul",
    age=23,
    city="Kolkata"
)

print(user)


# The extra city field is ignored and is not stored in the model.