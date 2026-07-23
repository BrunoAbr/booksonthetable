from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.book import Book, BookCreate
from app.services.book_service import get_books, create_book
from app.core.dependencies import get_db


router = APIRouter()

@router.get("/books")
def list_books(db: Session = Depends(get_db)):
    return get_books()

@router.post("/books", response_model=Book)
def add_book(book: BookCreate):
    return create_book(book)
