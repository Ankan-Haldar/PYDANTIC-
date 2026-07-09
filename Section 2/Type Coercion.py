from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    salary: float


employee = Employee(
    name="Amit",
    age="25",
    salary="45000.50"
)

print(employee)
print(type(employee.age))
print(type(employee.salary))


# The string "25" was converted into an integer, and "45000.50" was converted into a float.