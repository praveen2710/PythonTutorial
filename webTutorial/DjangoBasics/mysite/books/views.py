from django.shortcuts import render


from django.template import loader

# Create your views here.

##import this to add response
from django.http import HttpResponse
from .models import Book

def index(request):
    all_books = Book.objects.all()
    # this will let us  import html templates
    template = loader.get_template('books/index.html')
    context = {
        'all_books' : all_books
    }
    return HttpResponse(template.render(context, request))

def detail(request,book_id):
    return HttpResponse("<h2> Details for book Id:" + str(book_id) + "</h2>")