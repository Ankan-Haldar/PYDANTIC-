from uuid import UUID
from pydantic import BaseModel


class User(BaseModel):
    user_id: UUID
    name: str


user = User(
    user_id="550e8400-e29b-41d4-a716-446655440000",
    name="Rahul"
)

print(user)
print(type(user.user_id))



# Pydantic validates the UUID string and converts it into a Python UUID object