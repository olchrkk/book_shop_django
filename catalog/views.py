from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        books = Book.objects.all()
        authors = Author.objects.all()
        booksCount = books.count()
        authorsCount = authors.count()
        params = {
            'books': books,
            'booksCount': booksCount,
            'authorsCount': authorsCount
        }
        return render(request, self.template_name, params)
