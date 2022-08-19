from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    favorite_movies = models.ManyToManyField('movies.Movie')

    def __str__(self):
        return f'User: {self.username, self.favorite_movies}'
