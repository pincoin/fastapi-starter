from typing import Optional

from pydantic import BaseModel, Field


# Pydantic models delcaration
class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
    complete: bool
