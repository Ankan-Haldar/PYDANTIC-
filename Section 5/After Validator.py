from pydantic import BaseModel, field_validator


class Student(BaseModel):
    marks: int

    @field_validator("marks", mode="after")
    @classmethod
    def validate_marks(cls, value):
        if value < 0 or value > 100:
            raise ValueError(
                "Marks must be between 0 and 100"
            )

        return value


student = Student(
    marks=85
)

print(student)



# Standard Pydantic validation happens first. The custom validator then checks whether the validated integer is within the required range.