from pydantic import BaseModel, StrictInt


class User(BaseModel):
    name: str
    age: StrictInt


user = User(
    name="Rahul",
    age="25"
)


# StrictInt requires an actual integer value. The string "25" is not automatically converted.