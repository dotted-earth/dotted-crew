from pydantic import BaseModel
from typing import Union


class Law(BaseModel):
    name: str
    description: str
