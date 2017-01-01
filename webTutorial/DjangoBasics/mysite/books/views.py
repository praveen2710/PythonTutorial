from django.shortcuts import render

# Create your views here.

##import this to add response
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h>This is the books home page</h>")