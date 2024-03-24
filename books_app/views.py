from django.shortcuts import render

# Create your views here.


def __getBooks():
    return [
        {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Classic', 'status':'متاح', 'price': 15, 'image_url': 'https://example.com/images/gatsby.jpg'},
        {'id': 2, 'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian','status':'متاح', 'price': 12, 'image_url': 'https://example.com/images/1984.jpg'},
        {'id': 3, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Classic', 'status':'متاح', 'price': 18, 'image_url': 'https://example.com/images/mockingbird.jpg'},
        {'id': 4, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Classic', 'status':'متاح', 'price': 10, 'image_url': 'https://example.com/images/catcher.jpg'},
        {'id': 5, 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'status':'متاح', 'price': 20, 'image_url': 'https://example.com/images/hobbit.jpg'},
        {'id': 6, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance', 'status':'متاح', 'price': 14, 'image_url': 'https://example.com/images/pride.jpg'}
    ]
def listBooks(request):
    books = __getBooks()
    return render(request, 'pages/books.html', {'books': books})