
import enum

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship

from .base import Base


class OrderStatus(str, enum.Enum):
    NOT_ACCEPTED = "not accepted"
    ACCEPTED = "accepted"
    IN_PREPARATION = "in preparation"
    ON_ROUTE = "on route"
    DELIVERED = "delivered"


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(10), nullable=False, index=True)
    purchased_at = Column(DateTime, nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    customer = relationship("Customer", back_populates="orders")
    final_price = Column(Integer, nullable=False)
    status = Column(Enum(OrderStatus), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        server_onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
