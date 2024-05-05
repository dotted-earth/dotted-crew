from pydantic import BaseModel
from typing import Union


class Itinerary(BaseModel):
    id: str
    created_date: str
    start_date: str
    end_date: str
    length_of_stay: str
    destination: str
    budget: Union[int, None]
    itinerary_status: str
    user_id: str
    media_id: int
