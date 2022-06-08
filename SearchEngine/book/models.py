from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name='Author Name: ', 
                max_length=300, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(verbose_name='Book Title: ',
                max_length=300, blank=False, null= False)
    author = models.ManyToManyField(Author,verbose_name="Author: ",
                related_name='book')
    page = models.PositiveIntegerField(verbose_name="Number of Pages:",
                blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    