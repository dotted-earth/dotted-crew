from pydantic import BaseModel, Field
from typing import Union


class Meal(BaseModel):
    type: Union["breakfast", "brunch", "lunch", "late_lunch", "dinner", "late_dinner"] = Field(description="The type of meal")
    name: str = Field("The name of the dish")
    description: str = Field("A description of what the dish's ingredients are")
    cuisine: str = Field(description="The origin of the cuisine", )
