from app.schemas.book import BookBase, BookCreate, BookResponse
from app.repositories import book_repository
from sqlalchemy.orm import Session




def get_books(db: Session) -> list[BookResponse]:
    
    all_books = book_repository.find_all(db)

    books_response = []

    for book in all_books:
        books_response.append(
            BookResponse(
                id=book.id,
                title=book.title,
                author=book.author,
                pages=book.pages,
                rating=book.rating
            )
        )
    return books_response

def create_book(db: Session, book: BookCreate) -> BookResponse:
    books_model = book_repository.create(db, book)

    return BookResponse(
        id = books_model.id,
        title = books_model.title,
        author = books_model.author,
        pages = books_model.pages,
        rating = books_model.rating
    )
