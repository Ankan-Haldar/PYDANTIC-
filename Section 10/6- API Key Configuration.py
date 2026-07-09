from pydantic import HttpUrl, SecretStr

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )

    api_key: SecretStr
    api_url: HttpUrl


settings = Settings()


print(settings)


# SecretStr hides the API key when the settings object is printed, while HttpUrl validates the service URL.