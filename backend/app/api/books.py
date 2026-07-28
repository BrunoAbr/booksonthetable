from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.book import BookBase, BookCreate, BookResponse, BookUpdate
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

@router.delete("/books/{book_id}", status_code=204)
def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book_service.delete_book(db, book_id)

@router.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    return book_service.update_book(db, book_id, book_data) 
