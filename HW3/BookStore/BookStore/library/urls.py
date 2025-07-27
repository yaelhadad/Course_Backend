from django.urls import path
from . import views
from .views import BookListView

urlpatterns = [
    path('books-by-author/', views.books_by_author, name='books_by_author'),
    path('books-by-genre/', views.books_by_genre, name='books_by_genre'),
    path('books-count-by-genre/', views.books_count_by_genre, name='books_count_by_genre'),
    path('books/', BookListView.as_view(), name='book_list'),


]