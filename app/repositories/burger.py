from datetime import datetime
from typing import Optional

from sqlalchemy import func, select

from .base import BurgerApiRepository
from app.models import Burger
from app.models.burger import BreadTypes


class BurgersRepository(BurgerApiRepository):
    # Repository to handle burger CRUD
    def get_burgers(
        self,
    ) -> list[Burger]:

        query = select(Burger).where(Burger.deleted_at.is_(None))

        burgers = self.db.execute(query).scalars().all()

        return burgers

    def get_store_front_burgers(
        self,
    ) -> list[Burger]:

        query = select(Burger).where(
            Burger.is_store_front.is_(True), Burger.deleted_at.is_(None))

        burgers = self.db.execute(query).scalars().all()

        return burgers

    def create_burger(
        self,
        *,
        slug: str,
        name: str,
        description: str,
        bread_type: BreadTypes,
        base_price: int,
        is_store_front: bool,
        index_in_store: Optional[int] = 1,
        created_by_user_id: Optional[int] = None,
    ) -> Burger:
        burger = Burger(
            slug=slug,
            name=name,
            description=description,
            bread_type=bread_type,
            base_price=base_price,
            is_store_front=is_store_front,
            index_in_store=index_in_store,
            created_by_user_id=created_by_user_id,
        )

        self.db.add(burger)
        self.db.commit()

        return burger
    
    def get_burger_by_slug(
        self,
        burger_slug: str
    ) -> Burger:
        burger: Optional[Burger] = self.db.execute(
            select(Burger).where(
                Burger.slug == burger_slug,
                Burger.deleted_at.is_(None),
            )
        ).scalar_one_or_none()

        return burger

    def update_burger(
        self,
        burger: Burger,
    ) -> Burger:
        self.db.add(burger)
        self.db.commit()

        return burger
