from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
def list_books():
    return [
        {
            "id": 1,
            "title": "Revolução dos Bixos",
            "author": "George Orwell",
            "rating": 5
        }
    ]