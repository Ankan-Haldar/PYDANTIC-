from pydantic import BaseModel, Field


class Employee(BaseModel):
    employee_id: str = Field(
        pattern=r"^EMP-\d{4}$"
    )


employee = Employee(
    employee_id="EMP-1234"
)

print(employee)

# The value follows the required format: EMP- followed by exactly four digits.