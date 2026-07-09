from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    marks: float


student = Student(
    name="Rahul",
    age=22,
    marks=85.5
)

print(student)