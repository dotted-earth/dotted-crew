from pydantic import BaseModel


class Address(BaseModel):
    street1: str
    street2: str
    city: str
    state: str
    country: str
    postal_code: str
