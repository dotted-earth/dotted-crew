from pydantic import BaseModel

from src.models.address import Address


class Location(BaseModel):
    name: str
    address: Address
    lat: float
    lon: float
