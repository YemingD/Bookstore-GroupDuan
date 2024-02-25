from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=32)


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    authors = models.ManyToManyField("Author")


