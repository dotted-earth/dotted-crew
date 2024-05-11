import datetime
from typing import List, Union
from pydantic import BaseModel

from src.models.enums import ScheduleLineItemEnum
from src.models.location import Location


class ScheduleLineItem(BaseModel):
    name: str
    description: str
    schedule_type: ScheduleLineItemEnum
    start_location: Location
    end_location: Union[Location | None] = None
    start_time: datetime.time
    end_time: datetime.time
    duration: datetime.time
    estimated_price: Union[float | None] = None
    alternatives: List["ScheduleLineItem"] = []


ScheduleLineItem.model_rebuild()
