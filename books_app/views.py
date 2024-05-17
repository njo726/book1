from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Avg
from .models import Book
from .forms import BookForm

def listBooks(request):
    books = Book.objects.all().order_by('title')
    search_query = request.GET.get('search_name', '')
    genre_query = request.GET.get('genre', '')

    if search_query:
        books = books.filter(title__icontains=search_query) | books.filter(genre__icontains=search_query)
    if genre_query and not search_query:
        books = books.filter(genre__icontains=genre_query)

    total_books = Book.objects.count()
    average_price = Book.objects.aggregate(Avg('price'))['price__avg']
    books_by_status = Book.objects.values('status').annotate(total=Count('status')).order_by('status')

    context = {
        'books': books,
        'total_books': total_books,
        'average_price': average_price,
        'books_by_status': books_by_status,
        'form': BookForm()
    }
    return render(request, 'pages/books.html', context)

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listBooks')  # Assuming 'listBooks' is the name of the URL pattern for listing books
    else:
        form = BookForm()

    books = Book.objects.all().order_by('title')
    total_books = Book.objects.count()
    average_price = Book.objects.aggregate(Avg('price'))['price__avg']
    books_by_status = Book.objects.values('status').annotate(total=Count('status')).order_by('status')

    context = {
        'books': books,
        'total_books': total_books,
        'average_price': average_price,
        'books_by_status': books_by_status,
        'form': form
    }
    return render(request, 'pages/books.html', context)
