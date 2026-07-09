from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My App"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000


settings = Settings()


print(settings)



# Default values are used when no matching environment variables are available.