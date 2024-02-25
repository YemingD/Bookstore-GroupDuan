from django.contrib import admin
from .models import *


class BookModal(admin.StackedInline):
    model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', "author")
    fields = ('title', 'price', "authors")
    search_fields = ['title', 'price']

    def author(self, obj):
        return [author.name for author in obj.authors.all()]


    filter_horizontal = ('authors',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'books')
    search_fields = ['name']

    def books(self, obj):
        return [book.title for book in obj.book_set.all()]

