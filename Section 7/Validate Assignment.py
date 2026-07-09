from pydantic import BaseModel, ConfigDict


class Student(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True
    )

    name: str
    marks: int


student = Student(
    name="Rahul",
    marks=85
)


student.marks = "90"

print(student)
print(type(student.marks))


# Assignment validation is enabled, so the new value is validated and the compatible string "90" is converted into an integer.