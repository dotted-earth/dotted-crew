from pydantic import BaseModel, Field

class Address(BaseModel):
    street1: str = Field(description="The street number and name")
    street2: str = Field(description="Optional street number like apartment, unit, suite, etc.")
    city: str = Field(description="The city name")
    state: str = Field(description="The state name")
    country: str = Field(description="The country name")
    postal_code: str = Field(description="The postal code identifier")
