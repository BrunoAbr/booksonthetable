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

def find_by_id(db: Session, book_id: int) -> BookModel | None:
    statement =  select(BookModel).where(BookModel.id == book_id)

    result = db.execute(statement)

    return result.scalar_one_or_none()
