
from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from pydantic import Required

from app.core.helpers.slug import create_slug
from app.dependencies import get_burger_api_repository
from app.repositories import IngredientsRepository
from app.schemas import IngredientResponse, EditIngredientRequest, CreateIngredientRequest,  ErrorDetail

router = APIRouter()

@router.get(
    "/{ingredient_slug}/",
    response_model=IngredientResponse,
    responses={404: {"model": ErrorDetail, "description": "Ingredient not found"}},
)
async def get_ingredient_by_slug(
    ingredient_slug: str,
    ingredients_repo: IngredientsRepository = Depends(
        get_burger_api_repository(IngredientsRepository)
    ),
):
    ingredient = ingredients_repo.get_ingredient_by_slug(ingredient_slug)

    if not ingredient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": (
                    f"No ingredient found"
                )
            },
        )

    return ingredient

@router.get(
    "/",
    response_model=list[IngredientResponse],
    responses={404: {"model": ErrorDetail, "description": "Ingredients not found"}},
)
async def get_ingredients(
    ingredients_repo: IngredientsRepository = Depends(
        get_burger_api_repository(IngredientsRepository)
    ),
):
    ingredients = ingredients_repo.get_ingredients()

    if not ingredients:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": (
                    f"No ingredients found"
                )
            },
        )

    return ingredients


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=IngredientResponse,
)
async def create_ingredient(
    ingredient_payload: CreateIngredientRequest,
    ingredients_repo: IngredientsRepository = Depends(
        get_burger_api_repository(IngredientsRepository)
    ),
):
    ingredient = ingredients_repo.create_ingredient(
        **ingredient_payload.dict(),
        slug=create_slug(),
    )

    return ingredient


@router.patch(
    "/{ingredient_slug}/",
    status_code=status.HTTP_200_OK,
    response_model=IngredientResponse,
    responses={404: {"model": ErrorDetail, "description": "Ingredient not found"}},
)
async def edit_ingredient(
    ingredient_slug: str,
    ingredient_payload: EditIngredientRequest,
    ingredients_repo: IngredientsRepository = Depends(
        get_burger_api_repository(IngredientsRepository)
    ),
):
    ingredient = ingredients_repo.get_ingredient_by_slug(ingredient_slug)

    if not ingredient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": f"No ingredient found for {ingredient_slug} or has been eliminated."
            },
        )

    new_ingredient_data = ingredient_payload.dict(exclude_unset=True)
    for key, value in new_ingredient_data.items():
        setattr(ingredient, key, value)

    edited_ingredient = ingredients_repo.update_ingredient(ingredient)

    return edited_ingredient
