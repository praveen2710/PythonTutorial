from django.shortcuts import render

# Create your views here.

##import this to add response
from django.http import HttpResponse
from .models import Book

def index(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        url = '/books/' + str(book.id) + '/'
        html+='<a href="'+url+'">' + str(book.name) + '</a><br>'
    return HttpResponse(html)

def detail(request,book_id):
    return HttpResponse("<h2> Details for book Id:" + str(book_id) + "</h2>")