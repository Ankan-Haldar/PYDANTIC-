from pydantic import BaseModel


class User(BaseModel):
    name: str
    country: str = "India"


user = User(
    name="Rahul"
)

print(user)

# Since country was not provided, Pydantic automatically uses the default value "India".