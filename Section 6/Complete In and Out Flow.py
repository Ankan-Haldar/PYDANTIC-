from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    salary: float


raw_data = {
    "name": "Amit",
    "age": "25",
    "salary": "45000.50"
}


employee = Employee.model_validate(raw_data)


dictionary_output = employee.model_dump()


json_output = employee.model_dump_json()


print(employee)
print(dictionary_output)
print(json_output)


# This example shows the complete flow: raw dictionary data is validated into a model, then serialized into both dictionary and JSON formats.