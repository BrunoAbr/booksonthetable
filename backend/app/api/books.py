from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.book import BookBase, BookCreate, BookResponse
from app.services.book_service import get_books, create_book
from app.core.dependencies import get_db


router = APIRouter()

@router.get("/books", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):

    return get_books(db)

@router.post("/books", response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)
