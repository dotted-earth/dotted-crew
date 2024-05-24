from pydantic import BaseModel, Field


class Culture(BaseModel):
    name: str = Field(description="The name of the cultural behavior")
    description: str = Field(description="A brief description of the culture's significance and history")
