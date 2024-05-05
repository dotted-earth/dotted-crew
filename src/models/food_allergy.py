from pydantic import BaseModel
from typing import Union


class FoodAllergy(BaseModel):
    id: str
    created_date: str
    name: str
    description: Union[str, None]
