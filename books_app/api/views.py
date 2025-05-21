from rest_framework import generics
from rest_framework import viewsets
from books_app.models import Book
from .serializers import BookSerializer


class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
