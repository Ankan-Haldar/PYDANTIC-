from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        frozen=True
    )

    name: str
    age: int


user = User(
    name="Rahul",
    age=23
)


user.age = 24


# The model is immutable. Its field values cannot be reassigned after creation.