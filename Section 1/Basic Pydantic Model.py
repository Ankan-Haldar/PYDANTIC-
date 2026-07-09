from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


user = User(
    name="Rahul",
    age=25
)

print(user)



# User inherits from BaseModel. The model expects name as a string and age as an integer. Since both values are valid, the object is created successfully.