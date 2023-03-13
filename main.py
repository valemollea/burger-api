import uvicorn
from fastapi import FastAPI

from app.endpoints.burger import router as burger_router
from app.endpoints.ingredient import router as ingredient_router

app = FastAPI()

app.include_router(burger_router, prefix="/api/burger", tags=["Burgers"])
app.include_router(ingredient_router, prefix="/api/ingredient", tags=["Ingredients"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)