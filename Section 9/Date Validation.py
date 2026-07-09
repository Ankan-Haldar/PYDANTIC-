from datetime import date
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    joining_date: date


student = Student(
    name="Rahul",
    joining_date="2026-07-09"
)

print(student)
print(type(student.joining_date))




# The ISO-format date string is parsed into a Python date object.