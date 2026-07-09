from pydantic import BaseModel


class Student(BaseModel):
    name: str
    marks: list[int]


student = Student(
    name="Rahul",
    marks=[80, 85, 90]
)

print(student)


# The marks field expects a list of integers. Pydantic validates every value inside the list.