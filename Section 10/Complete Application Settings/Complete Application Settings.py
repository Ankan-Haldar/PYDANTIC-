from pydantic import SecretStr

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )

    app_name: str
    environment: str
    debug: bool
    host: str
    port: int
    database_url: str
    api_key: SecretStr


settings = Settings()


print(settings.app_name)
print(settings.environment)
print(settings.debug)
print(settings.host)
print(settings.port)
print(settings.database_url)
print(settings.api_key)




# The complete application configuration is loaded from the environment, validated by Pydantic Settings, and made available through a structured settings object.