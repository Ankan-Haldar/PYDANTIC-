# First----> pip install pydantic-settings


from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    debug: bool
    port: int


settings = Settings(
    app_name="My Application",
    debug=True,
    port=8000
)


print(settings)


# BaseSettings creates a validated configuration object similar to a normal Pydantic model.