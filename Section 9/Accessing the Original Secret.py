from pydantic import BaseModel, SecretStr


class APIConfig(BaseModel):
    api_key: SecretStr


config = APIConfig(
    api_key="secret-api-key-123"
)


print(config.api_key)

print(
    config.api_key.get_secret_value()
)



# The secret remains hidden by default. get_secret_value() explicitly returns the original value when the application genuinely needs it.