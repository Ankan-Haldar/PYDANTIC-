from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    name: str
    age: int


user = User(
    name="Rahul",
    age=23,
    city="Kolkata"
)


# The city field is not defined in the model. Since extra="forbid" is enabled, Pydantic rejects the extra field.