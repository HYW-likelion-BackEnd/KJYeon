# cbv
# from django.urls import path
# from .views import BookAPI, BooksAPI

# fbv
from django.urls import path
from .views import bookAPI, booksAPI

urlpatterns = [
    # cbv
    # path('cbv/books/', BooksAPI.as_view()),
    # path('cbv/book/<int:bid>/', BookAPI.as_view()),

    # fbv
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
]