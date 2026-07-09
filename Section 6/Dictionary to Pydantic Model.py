from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


data = {
    "name": "Rahul",
    "age": "23"
}


user = User.model_validate(data)

print(user)



# model_validate() validates the dictionary and creates a User model. The string "23" is converted into an integer.