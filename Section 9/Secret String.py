from pydantic import BaseModel, SecretStr


class Account(BaseModel):
    username: str
    password: SecretStr


account = Account(
    username="rahul123",
    password="mySecretPassword"
)

print(account)
print(account.password)

# SecretStr hides the actual password when the model or field is printed.