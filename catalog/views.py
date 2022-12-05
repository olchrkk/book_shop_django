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

class BookView(TemplateView):
    template_name = 'catalog/book.html'

    def get(self, request, id):
        book = Book.objects.get(id=id)
        params = {
            'book': book
        }
        return render(request, self.template_name, params)
