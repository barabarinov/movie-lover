from django.contrib import admin

from .models import Movie, Genre, Country

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Country)
