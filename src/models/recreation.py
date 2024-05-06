from pydantic import BaseModel
from typing import Union


class Recreation(BaseModel):
    id: str
    created_date: str
    name: str
    description: Union[str, None]
