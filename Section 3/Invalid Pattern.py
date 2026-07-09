from pydantic import BaseModel, Field


class Employee(BaseModel):
    employee_id: str = Field(
        pattern=r"^EMP-\d{4}$"
    )


employee = Employee(
    employee_id="EMP-123"
)


# The ID contains only two digits after EMP-, while the pattern requires exactly four digits.