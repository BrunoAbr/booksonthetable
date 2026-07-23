from pydantic import BaseModel

class BookBase(BaseModel):
    id: int
    title: str
    author: str
    pages: int
    rating: float

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int