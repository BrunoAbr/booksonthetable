from django.shortcuts import render
from django.http import HttpResponse
import requests

def books(request):

    response = requests.get("http://127.0.0.1:8001/books")

    books = response.json()

    print(books)

    return render(request, "books/books.html", {"books": books})

