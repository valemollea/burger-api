
import enum

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Integer,
    String,
    Text,
    func,
)

from .base import Base


class IngredientTypes(str, enum.Enum):
    PATTY = "patty"
    VEGETABLE = "vegetable"
    SAUCE = "sauce"
    TOPPING = "topping"


class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(10), nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    type = Column(Enum(IngredientTypes), nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        server_onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
