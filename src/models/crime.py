from pydantic import BaseModel


class Crime(BaseModel):
    name: str
    description: str
