import datetime
from typing import List, Union
from pydantic import BaseModel

from src.models.schedule_line_item import ScheduleLineItem
from src.models.enums import ScheduleLengthEnum, ScheduleIntensityEnum


class Schedule(BaseModel):
    name: str
    description: str
    schedule_intensity: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    schedule_intensity: ScheduleIntensityEnum
    schedule_length: ScheduleLengthEnum
    schedule_line_items: List[ScheduleLineItem] = []
    estimated_cost: Union[float | None] = None
