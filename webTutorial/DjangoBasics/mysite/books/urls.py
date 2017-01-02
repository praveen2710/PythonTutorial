from django.conf.urls import url
from django.contrib import admin
#this imports from current directory.
from . import views

##this will redirect it to views file index method
## the pattern is what redirect to specific view if multiple views are present
app_name = 'books'

urlpatterns = [
    ####url(r'^$',views.index,name='index'),
    #/books/2
    ####url(r'^(?P<book_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^$',views.IndexView.as_view(),name='index'),
    # /books/2
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

    url(r'^add-book/$',views.BookCreate.as_view(),name='book-add'),
]
