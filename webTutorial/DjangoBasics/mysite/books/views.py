from django.shortcuts import render


####from django.template import loader

# Create your views here.

##import this to add response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.http import Http404


def index(request):
    all_books = Book.objects.all()
    # this will let us  import html templates
    ####template = loader.get_template('books/index.html')
    context = {
        'all_books' : all_books
    }
    #better way than using template or httpresponse
    return render(request,'books/index.html',context)

def detail(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
        ##for exception check Class not object also DoesNotExist not Exists
    except Book.DoesNotExist:
        raise Http404("This book does not exist")
    ####return HttpResponse("<h2> Details for book Id:" + str(book_id) + "</h2>")
    return render(request,'books/detail.html',{'book':book})