from attrs import define

from app.models import SessionLocal as BurgerApiSessionLocal


@define
class BurgerApiRepository:
    db: BurgerApiSessionLocal
