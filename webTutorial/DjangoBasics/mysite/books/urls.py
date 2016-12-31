from django.conf.urls import url
from django.contrib import admin
#this imports from current directory.
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
