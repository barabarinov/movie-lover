from django.urls import path
from .views import MovieDetailView, MoviesListView, RateMovieView

app_name = 'movies'

urlpatterns = [
    path('', MoviesListView.as_view(), name='list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('<int:pk>/rate/', RateMovieView.as_view(), name='rate'),
]
