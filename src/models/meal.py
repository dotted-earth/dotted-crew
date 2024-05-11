from pydantic import BaseModel
from typing import Union


class Meal(BaseModel):
    type: Union["breakfast", "brunch", "lunch", "late_lunch", "dinner", "late_dinner"]
    name: str
    description: str
    location: str
