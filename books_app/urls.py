from django.urls import path
from . import views
urlpatterns = [
    path('', views.listBooks, name='listBooks'),
]
