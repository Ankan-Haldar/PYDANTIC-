from pydantic import BaseModel, Field


class Offer(BaseModel):
    product: str
    discount: float = Field(ge=0, lt=100)


offer = Offer(
    product="Laptop",
    discount=25
)

print(offer)

# The discount must be at least 0 and strictly less than 100.