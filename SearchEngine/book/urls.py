from os import name
from django.urls import path
from .views import BookList, Search

urlpatterns = [
    path('', BookList.as_view(), name='bookList'),
    path('search-book/', Search.as_view(), name='searchEngine')
]