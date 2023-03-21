from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import date


class BookInterface(BaseModel):
    id: int
    name: str
    author: str
    category: str
    year: date
    gender: str
    publish_company: str


class BooksOutput(BaseModel):
    previus_page: int
    next_page: int
    total_page: int
    books: List[BookInterface] = Field(default_factory=list)


class BooksCreateInput(BaseModel):
    books: List[BookInterface] = Field(default_factory=list)


class BooksCreateOutput(BaseModel):
    code: int
    message: str


class BooksDeleteOutput(BaseModel):
    code: int
    message: str


class BooksUpdateInfoInput(BaseModel):
    id: int
    name: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    year: Optional[date] = None
    gender: Optional[str] = None
    publish_company: Optional[str] = None
