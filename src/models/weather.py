from pydantic import BaseModel
from typing import Union


class Weather(BaseModel):
    date: str
    temp: float
    scale: Union["fahrenheit", "celsius"]
