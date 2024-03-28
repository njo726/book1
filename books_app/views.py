from django.shortcuts import render
from .models import Book  # Make sure to import your Book model

def listBooks(request):
    # Get books from the database
    books = Book.objects.all().order_by('title')
    # Get search parameters from the GET request
    search_query = request.GET.get('search_name', '')
    genre_query = request.GET.get('genre', '')

    # Filter books based on the search query
    if search_query:
        books = books.filter(title__icontains=search_query) | books.filter(genre__icontains=search_query)

    # Filter books based on the genre query (only if there's no search query)
    if genre_query and not search_query:
        books = books.filter(genre__icontains=genre_query)

    # Render the page with the filtered books
    return render(request, 'pages/books.html', {'books': books})
