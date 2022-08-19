from django.urls import path, include
from .views import MovieDetailView, MoviesListView, RateMovieView

app_name = 'movies'

urlpatterns = [
    path('', MoviesListView.as_view(), name='list'),
    path('<int:pk>/', include('crew.urls')),

    path('<int:pk>/rate/', RateMovieView.as_view(), name='rate'),
]
