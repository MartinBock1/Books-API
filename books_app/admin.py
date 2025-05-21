from django.contrib import admin
from .models import Book

list_display = ('titel', 'autor', 'price')

# Register your models here.
admin.site.register(Book)
