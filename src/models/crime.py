from pydantic import BaseModel, Field


class Crime(BaseModel):
    name: str = Field(description="The name of the crime like petty theft, assaults, etc.")
    description: str = Field(description="A description of the common crime being committed")
