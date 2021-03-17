from django.db import models


class Library(models.Model):

    name = models.CharField(max_length=100)


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('book.Author', on_delete=models.CASCADE)
    libraries = models.ManyToManyField('book.Library')


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Leads(models.Model):

    email = models.EmailField(max_length = 254) 
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    library = models.ForeignKey('book.Library', on_delete=models.CASCADE)