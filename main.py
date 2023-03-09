import uvicorn
from fastapi import FastAPI

from app.endpoints.burger import router as burger_router

app = FastAPI()

app.include_router(burger_router, prefix="/api/burger", tags=["Burgers"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)