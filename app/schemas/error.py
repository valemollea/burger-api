from pydantic import BaseModel


class ErrorMessage(BaseModel):
    error: str


class ErrorDetail(BaseModel):
    detail: ErrorMessage
