from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str
    age: int = Field(ge=5, le=100)


student = Student(
    name="Amit",
    age=22
)

print(student)