from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    FICTION = 'Fiction'
    NONFICTION = 'Non-Fiction'
    SCIFI = 'Science Fiction'
    FANTASY = 'Fantasy'
    MYSTERY = 'Mystery'
    BIOGRAPHY = 'Biography'

    GENRE_CHOICES = [
        (FICTION, 'Fiction'),
        (NONFICTION, 'Non-Fiction'),
        (SCIFI, 'Science Fiction'),
        (FANTASY, 'Fantasy'),
        (MYSTERY, 'Mystery'),
        (BIOGRAPHY, 'Biography'),
    ]

    name = models.CharField(max_length=50, choices=GENRE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=3  # default rating if none is given
    )

    @staticmethod
    def total_books():
        return Book.objects.count()


    def __str__(self):
        return self.title



