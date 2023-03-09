from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt

from app.models.burger import BreadTypes


class CreateBurgerRequest(BaseModel):
    name: str
    description: str
    bread_type: BreadTypes
    base_price: PositiveInt
    is_store_front: bool
    index_in_store: Optional[int] = 1
    created_by_user_id: Optional[int]

    class Config:
        extra = "forbid"


class EditBurgerRequest(BaseModel):
    name: Optional[str]
    description: Optional[str]
    bread_type: Optional[BreadTypes]
    base_price: Optional[PositiveInt]
    is_store_front: Optional[bool]
    index_in_store: Optional[int]
    created_by_user_id: Optional[int]

    class Config:
        extra = "forbid"


class BurgerResponse(BaseModel):
    id: int
    slug: str

    name: str
    description: str
    bread_type: BreadTypes
    base_price: PositiveInt
    is_store_front: bool
    index_in_store: Optional[int] = 1
    created_by_user_id: Optional[int]

    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
