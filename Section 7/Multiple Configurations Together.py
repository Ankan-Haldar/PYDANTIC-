from pydantic import BaseModel, ConfigDict


class Account(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        str_to_lower=True
    )

    username: str
    email: str


account = Account(
    username="   ANKAN123   ",
    email="   ANKAN@EXAMPLE.COM   "
)


print(account)

# This model rejects extra fields, validates future assignments, removes surrounding whitespace, and converts string values to lowercase.