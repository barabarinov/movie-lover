from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = models.DateField(null=True, blank=True)
    country = models.ForeignKey(
        'movies.Country',
        related_name='directors',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Director: {self.first_name} {self.last_name} {self.country}'


class Actor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = models.DateField(null=True, blank=True)
    country = models.ForeignKey(
        'movies.Country',
        related_name='actors',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Actor: {self.first_name} {self.last_name} {self.country}'
