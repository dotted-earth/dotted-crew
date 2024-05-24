from pydantic import BaseModel, Field


class Law(BaseModel):
    name: str = Field(description="The name of the law")
    description: str = Field(description="A brief description in layman's term on the consequences of breaking the law")
