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


student.marks = "invalid"



# The new value cannot be converted into an integer, so assignment validation fails.