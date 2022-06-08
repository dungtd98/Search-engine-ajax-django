from django.shortcuts import render
from .models import Book, Author
from django.views.generic.list import ListView
from django.views import View
import json
from django.http import JsonResponse
# Create your views here.

class Search(View):
    def post(self, request):
        if self.request.method == 'POST':
            search_str = json.loads(request.body).get('searchText')
            book = Book.objects.filter(title__istartswith = search_str
            )|Book.objects.filter(author__istartswith = search_str)
            data = book.values()
            return JsonResponse(list(data), safe=False)

class BookList(ListView):
    model = Book
    template_name = 'book/booklist.html'
    context_object_name = 'books'