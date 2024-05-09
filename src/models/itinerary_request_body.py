import datetime
from pydantic import BaseModel
from typing import Union


class ItineraryRequestBody(BaseModel):
    id: int
    created_at: datetime.datetime
    start_date: datetime.datetime
    end_date: datetime.datetime
    length_of_stay: int
    destination: str
    budget: Union[int, None] = None
    itinerary_status: str
    user_id: str
    media_id: int
