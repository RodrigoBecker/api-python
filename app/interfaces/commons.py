from pydantic import BaseModel


class APIBadRequest(BaseModel):
    code: int
    message: str


class APIForbidden(BaseModel):
    code: int
    message: str
