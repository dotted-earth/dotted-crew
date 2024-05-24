from pydantic import BaseModel, Field
from typing import Union


class Weather(BaseModel):
    date: str = Field(description="The date in YYYY-MM-DD format")
    temp: float = Field(description="A floating number representing the temperature", examples="98.8 degrees F")
    scale: Union["fahrenheit", "celsius"] = Field(description="The scale of the temperature")
