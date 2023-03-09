
import enum

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)

from sqlalchemy.orm import relationship

from .base import Base


class BreadTypes(str, enum.Enum):
    SESAME_SEED = "sesame_seed"
    WHEAT = "wheat"
    POTATO = "potato"
    BRIOCHE = "brioche"


class Burger(Base):
    __tablename__ = "burgers"
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(10), nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    bread_type = Column(Enum(BreadTypes), nullable=False)
    base_price = Column(Integer, nullable=False)
    is_store_front = Column(Boolean, nullable=False)
    index_in_store = Column(Integer, default=1, nullable=False)
    created_by_user_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        server_onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)


class BurgerIngredientRelation(Base):
    __tablename__ = "burger_ingredient_relations"
    id = Column(Integer, primary_key=True, index=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    burger_id = Column(Integer, ForeignKey("burgers.id"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        server_onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    burger = relationship("Burger", backref="burger_ingredient")
    ingredient = relationship("Ingredient", backref="ingredient_burger")


class BurgerOrderRelation(Base):
    __tablename__ = "burger_order_relations"
    id = Column(Integer, primary_key=True, index=True)
    burger_id = Column(Integer, ForeignKey("burgers.id"), nullable=False)
    customer_id = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        server_onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    burger = relationship("Burger", backref="burger_order")
    order = relationship("Order", backref="order_burger")
