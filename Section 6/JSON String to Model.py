from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


json_data = '''
{
    "name": "Rahul",
    "age": 23
}
'''


user = User.model_validate_json(json_data)

print(user)


# model_validate_json() reads the JSON string, validates the values, and creates the model object.