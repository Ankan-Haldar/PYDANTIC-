from pydantic import BaseModel


class Course(BaseModel):
    title: str
    duration_months: int
    price: float
    instructor: str | None = None
    active: bool = True


course = Course(
    title="AI Engineering",
    duration_months="6",
    price="4999.50"
)

print(course)





# BaseModel creates the model structure; required fields must be provided; default fields are filled automatically when omitted; nullable fields can accept None; and compatible values may be converted through type coercion.