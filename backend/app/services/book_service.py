from app.schemas.book import Book, BookCreate
from app.repositories.book_repository import find_all, save
from sqlalchemy.orm import Session




def get_books() -> list[Book]:
    return find_all()

def create_book(book: BookCreate) -> Book:
    books = find_all()

    new_book = Book(
        id=len(books) +1,
        **book.model_dump()
    )

    return save(new_book)