from pydantic import BaseModel
from typing import Union
import datetime


class Cuisine(BaseModel):
    id: int
    created_at: datetime.datetime
    name: str
    description: Union[str, None]
