from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(default='')
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='movies_photo', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    director = models.ForeignKey(
        'crew.Director',
        related_name='movies',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    actors = models.ManyToManyField(
        'crew.Actor',
        related_name='movies',
    )
    genre = models.ManyToManyField(
        'movies.Genre',
        related_name='movies',
    )
    rates = models.ManyToManyField(
        User,
        through='movies.Rate',
        related_name='rated_movies',
    )
    country = models.ForeignKey(
        'movies.Country',
        related_name='movies',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0)
    date_rated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} rated for {self.movie} with {self.stars} stars'


# TODO move to core
class Country(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'Country: {self.name}'

    class Meta:
        verbose_name_plural = 'countries'
