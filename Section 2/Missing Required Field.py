from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int


student = Student(
    name="Rahul"
)

# age is a required field. Since no value was provided, Pydantic raises a validation error.