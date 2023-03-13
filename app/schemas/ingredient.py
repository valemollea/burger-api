from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt

from app.models.ingredient import IngredientTypes


class CreateIngredientRequest(BaseModel):
    name: str
    description: str
    type: IngredientTypes
    price: PositiveInt

    class Config:
        extra = "forbid"


class EditIngredientRequest(BaseModel):
    name: Optional[str]
    description: Optional[str]
    type: Optional[IngredientTypes]
    price: Optional[PositiveInt]

    class Config:
        extra = "forbid"


class IngredientResponse(BaseModel):
    id: int
    slug: str

    name: str
    description: str
    type: IngredientTypes
    price: PositiveInt

    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
