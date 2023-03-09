
from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from pydantic import Required

from app.core.helpers.slug import create_slug
from app.dependencies import get_burger_api_repository
from app.repositories import BurgersRepository
from app.schemas import BurgerResponse, CreateBurgerRequest, EditBurgerRequest,  ErrorDetail

router = APIRouter()

@router.get(
    "/{burger_slug}/",
    response_model=BurgerResponse,
    responses={404: {"model": ErrorDetail, "description": "Burger not found"}},
)
async def get_burger_by_slug(
    burger_slug: str,
    burgers_repo: BurgersRepository = Depends(
        get_burger_api_repository(BurgersRepository)
    ),
):
    burgers = burgers_repo.get_burger_by_slug(burger_slug)

    if not burgers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": (
                    f"No burgers found"
                )
            },
        )

    return burgers

@router.get(
    "/store-front/",
    response_model=list[BurgerResponse],
    responses={404: {"model": ErrorDetail, "description": "Burgers not found"}},
)
async def get_store_front_burgers(
    burgers_repo: BurgersRepository = Depends(
        get_burger_api_repository(BurgersRepository)
    ),
):
    burgers = burgers_repo.get_store_front_burgers()

    if not burgers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": (
                    f"No burgers found"
                )
            },
        )

    return burgers

@router.get(
    "/",
    response_model=list[BurgerResponse],
    responses={404: {"model": ErrorDetail, "description": "Burgers not found"}},
)
async def get_burgers(
    burgers_repo: BurgersRepository = Depends(
        get_burger_api_repository(BurgersRepository)
    ),
):
    burgers = burgers_repo.get_burgers()

    if not burgers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": (
                    f"No burgers found"
                )
            },
        )

    return burgers


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=BurgerResponse,
)
async def create_burger(
    burger_payload: CreateBurgerRequest,
    burgers_repo: BurgersRepository = Depends(
        get_burger_api_repository(BurgersRepository)
    ),
):
    burger = burgers_repo.create_burger(
        **burger_payload.dict(),
        slug=create_slug(),
    )

    return burger


@router.patch(
    "/{burger_slug}/",
    status_code=status.HTTP_200_OK,
    response_model=BurgerResponse,
    responses={404: {"model": ErrorDetail, "description": "Burgers not found"}},
)
async def edit_burger(
    burger_slug: str,
    burger_payload: EditBurgerRequest,
    burgers_repo: BurgersRepository = Depends(
        get_burger_api_repository(BurgersRepository)
    ),
):
    burger = burgers_repo.get_burger_by_slug(burger_slug)

    if not burger:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": f"No burger found for {burger_slug} or has been eliminated."
            },
        )

    new_burger_data = burger_payload.dict(exclude_unset=True)
    for key, value in new_burger_data.items():
        setattr(burger, key, value)

    edited_burger = burgers_repo.update_burger(burger)

    return edited_burger
