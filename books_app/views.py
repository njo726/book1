from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Count, Avg
from .models import Book
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

    total_books = Book.objects.count()
    average_price = Book.objects.aggregate(Avg('price'))['price__avg']
    books_by_status = Book.objects.values('status').annotate(total=Count('status')).order_by('status')

    context = {
        'books':books,
        'total_books': total_books,
        'average_price': average_price,
        'books_by_status': books_by_status,
    }
    return render(request, 'pages/books.html',context)

@csrf_exempt
def add_book(request):
    books = Book.objects.all().order_by('title')
    new_book = Book(
        title=request.POST['title'],
        author=request.POST['author'],
        genre=request.POST['genre'],
        status=request.POST['status'],
        price=request.POST.get('price', 0),  # Using get to provide a default if not supplied
        image_url=request.POST.get('image_url', '')  # Optional field
    )
    new_book.save()
    return redirect('pages/books.html') 

