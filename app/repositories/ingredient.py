from datetime import datetime
from typing import Optional

from sqlalchemy import func, select

from .base import BurgerApiRepository
from app.models import Ingredient
from app.models.ingredient import IngredientTypes


class IngredientsRepository(BurgerApiRepository):
    # Repository to handle ingredient CRUD
    def get_ingredients(
        self,
    ) -> list[Ingredient]:

        query = select(Ingredient).where(Ingredient.deleted_at.is_(None))

        ingredients = self.db.execute(query).scalars().all()

        return ingredients

    def create_ingredient(
        self,
        *,
        slug: str,
        name: str,
        description: str,
        type: IngredientTypes,
        price: int,
    ) -> Ingredient:
        ingredient = Ingredient(
            slug=slug,
            name=name,
            description=description,
            type=type,
            price=price,
        )

        self.db.add(ingredient)
        self.db.commit()

        return ingredient
    
    def get_ingredient_by_slug(
        self,
        ingredient_slug: str
    ) -> Ingredient:
        ingredient: Optional[Ingredient] = self.db.execute(
            select(Ingredient).where(
                Ingredient.slug == ingredient_slug,
                Ingredient.deleted_at.is_(None),
            )
        ).scalar_one_or_none()

        return ingredient

    def update_ingredient(
        self,
        ingredient: Ingredient,
    ) -> Ingredient:
        self.db.add(ingredient)
        self.db.commit()

        return ingredient
