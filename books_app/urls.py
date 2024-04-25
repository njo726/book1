from django.urls import path
from . import views
urlpatterns = [
    path('', views.listBooks, name='listBooks'),
        path('add_book', views.add_book, name='add_book'),  # URL to handle book creation

]
