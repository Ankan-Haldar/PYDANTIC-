from pydantic import BaseModel, ValidationError


class Student(BaseModel):
    name: str
    age: int


try:
    student = Student(
        name="Amit",
        age="wrong-age"
    )

except ValidationError as error:
    print(error)

    # The invalid age causes a validation error. Using try-except, the application can catch and handle the error instead of crashing unexpectedly.