from pydantic import BaseModel, Field

from src.models.address import Address


class Location(BaseModel):
    name: str = Field(description="The name of the location")
    address: Address
    lat: float = Field(description="The latitude of the location")
    lon: float = Field(description="The longitude of the location")


Location.model_rebuild()
