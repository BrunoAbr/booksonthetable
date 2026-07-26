from app.schemas.book import BookBase, BookCreate, BookResponse
from app.repositories import book_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException





def get_books(db: Session) -> list[BookResponse]:
    
    all_books = book_repository.find_all(db)


    return [
        BookResponse.model_validate(book)
        for book in all_books
    ]

def create_book(db: Session, book: BookCreate) -> BookResponse:
    books_model = book_repository.create(db, book)

    return BookResponse.model_validate(books_model)

def get_book(db: Session, book_id: int) -> BookResponse:
    book_found = book_repository.find_by_id(db, book_id)
    if (book_found is None):
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    else:
        return BookResponse.model_validate(book_found)

def delete_book(db: Session, book_id: int) -> None:
    book_found = book_repository.find_by_id(db, book_id)

    if (book_found is None):
        book_repository.delete(db, book_found)
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )