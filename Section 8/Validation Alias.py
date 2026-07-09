from pydantic import BaseModel, Field


class Employee(BaseModel):
    employee_id: int = Field(
        validation_alias="employeeId"
    )

    name: str


employee = Employee(
    employeeId=101,
    name="Rahul"
)


print(employee)



# The model accepts employeeId as the input key but stores the field internally as employee_id.