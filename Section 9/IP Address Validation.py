from pydantic import BaseModel
from pydantic.networks import IPvAnyAddress


class Server(BaseModel):
    name: str
    ip_address: IPvAnyAddress


server = Server(
    name="Main Server",
    ip_address="192.168.1.10"
)

print(server)


# Pydantic validates the IP address and converts it into the appropriate IP address object.