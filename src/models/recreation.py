from pydantic import BaseModel


class Recreation(BaseModel):
    id: str
    created_date: str
    name: str
    description: str | None
