from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.book import BookBase, BookCreate, BookResponse
from app.services import book_service
from app.core.dependencies import get_db


router = APIRouter()

@router.get("/books", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):

    return book_service.get_books(db)

@router.get("/books/{book_id}", response_model=BookResponse)
def book_by_id(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_book(db, book_id)


@router.post("/books", response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)

