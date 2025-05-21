from django.urls import path, include
from .views import BooksView, BooksViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', BooksViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('book/', BooksView.as_view()),
]
