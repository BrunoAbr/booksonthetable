from app.models.book import BookModel
from app.schemas.book import BookCreate
from sqlalchemy import select
from sqlalchemy.orm import Session


def find_all(db: Session) -> list[BookModel]:
    statement = select(BookModel)
    result = db.execute(statement)

    return result.scalars().all()

def create(db: Session, book: BookCreate) -> BookModel:
    book_model = BookModel(
        title = book.title,
        author = book.author,
        pages = book.pages,
        rating = book.rating
    )

    db.add(book_model)
    db.commit()
    db.refresh(book_model)

    return book_model