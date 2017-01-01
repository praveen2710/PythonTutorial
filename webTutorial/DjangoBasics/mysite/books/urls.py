from django.conf.urls import url
from django.contrib import admin
#this imports from current directory.
from . import views

##this will redirect it to views file index method
## the pattern is what redirect to specific view if multiple views are present
urlpatterns = [
    url(r'^$',views.index,name='index'),
]
