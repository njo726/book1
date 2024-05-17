from django.urls import path
from . import views
urlpatterns = [
    path('', views.listBooks, name='listBooks'),
        path('add_book', views.add_book, name='add_book'),  
         path('update/<int:pk>/', views.update_book, name='update_book'),
             path('delete/<int:pk>/', views.delete_book, name='delete_book'),


]

