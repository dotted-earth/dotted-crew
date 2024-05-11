from pydantic import BaseModel
from typing import Union


class Culture(BaseModel):
    name: str
    description: str
