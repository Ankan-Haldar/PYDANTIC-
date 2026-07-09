from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    marks: float
    course: str


student = Student(
    name="Rahul",
    age=23,
    marks=85.5,
    course="MCA"
)


data = student.model_dump(
    include={"name", "course"}
)

print(data)


# Only the name and course fields are included in the output.