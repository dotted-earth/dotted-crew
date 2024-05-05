from pydantic import BaseModel
from typing import Union


class Diet(BaseModel):
    id: str
    created_date: str
    name: str
    description: Union[str, None]
