from pydantic import BaseModel, computed_field


class User(BaseModel):
    first_name: str
    last_name: str

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


user = User(
    first_name="Ankan",
    last_name="Haldar"
)


print(user.full_name)



# full_name is calculated from first_name and last_name.