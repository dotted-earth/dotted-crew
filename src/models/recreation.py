import datetime
from pydantic import BaseModel
from typing import Union


class Recreation(BaseModel):
    id: int
    created_at: datetime.datetime
    name: str
    description: Union[str, None]
