from django.shortcuts import render
from .models import Author, Book, Genre
from django.db.models import Count
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.prefetch_related('authors', 'genre').all()


def books_by_author(request):
    authors = Author.objects.all()
    author_name = request.GET.get('author')
    books = []
    selected_author = None

    if author_name:
        try:
            first_name, last_name = author_name.split(' ', 1)
            selected_author = Author.objects.get(first_name=first_name, last_name=last_name)
            books = Book.objects.filter(authors=selected_author)
        except Author.DoesNotExist:
            selected_author = None

    context = {
        'authors': authors,
        'books': books,
        'selected_author': selected_author,
    }
    return render(request, 'books_by_author.html', context)

def books_by_genre(request):
    genres = Genre.objects.all()
    genre_name = request.GET.get('genre')
    books = []
    selected_genre = None

    if genre_name:
        try:
            selected_genre = Genre.objects.get(name=genre_name)
            books = Book.objects.filter(genre=selected_genre)
        except Genre.DoesNotExist:
            selected_genre = None

    return render(request, 'books_by_genre.html', {
        'genres': genres,
        'books': books,
        'selected_genre': selected_genre,
    })

def books_count_by_genre(request):
    genre_stats = Genre.objects.annotate(book_count=Count('book'))
    return render(request, 'books_count_by_genre.html', {'genre_stats': genre_stats})

