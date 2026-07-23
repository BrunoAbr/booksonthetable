from fastapi import FastAPI
from app.api.books import router as books_router
from app.models.book import BookModel
from app.core.database import Base, engine

app = FastAPI()


app.include_router(books_router)

Base.metadata.create_all(bind=engine)
