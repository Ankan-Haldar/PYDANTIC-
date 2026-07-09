from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )

    app_name: str
    debug: bool
    port: int


settings = Settings()


print(settings)



# SettingsConfigDict tells Pydantic Settings to read configuration values from the .env file.