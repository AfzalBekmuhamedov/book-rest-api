from django.urls import path
from .views import *

urlpatterns = [
    path("authors/",AuthorList.as_view()),
    path("authors/<int:pk>/",AuthorDetail.as_view()),
    path("books/", BookList.as_view()),
    path("books/<int:pk>/", BookDetail.as_view()),
]