from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    author: str
    pages: int
    rating: float

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    pages: int | None = None
    rating: float | None = None
    
