from __future__ import unicode_literals

from django.db import models

# Create your models here.

##class name is table name
class Book(models.Model):

    ##this will override string calls
    ##when call Book.objects.all() will show this
    def __str__(self):
        return self.name+'-'+self.author

    ##column name and attribures
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)



#class table_name(models.Model):
   #columnname = models.column_Type(attributes)

