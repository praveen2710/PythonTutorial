##this is generic view implementation of views
from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

class BookCreate(CreateView):
    model = Book
    fields = ['name','author','price','type','book_image']