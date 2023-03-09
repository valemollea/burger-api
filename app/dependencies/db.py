from typing import Callable, Type

from fastapi import Depends

from app.models import SessionLocal as BurgerApiSessionLocal
from app.repositories import BurgerApiRepository


async def get_burger_api_db():
    try:
        db = BurgerApiSessionLocal()
        yield db
    finally:
        db.close()


def get_burger_api_repository(
    repo_cls: Type[BurgerApiRepository],
) -> Callable[[BurgerApiSessionLocal], BurgerApiRepository]:
    def _get_repo(db: BurgerApiSessionLocal = Depends(get_burger_api_db)) -> BurgerApiRepository:
        return repo_cls(db)

    return _get_repo
