from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from movies.models import Movie, Rate
from movies.forms import RateMovieForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MoviesListView(ListView):
    model = Movie

    template_name = 'movies/list.html'
    context_object_name = 'movies'

    ordering = '-created_at'
    paginate_by = 10


class MovieDetailView(DetailView):
    model = Movie

    template_name = 'movies/detail.html'
    context_object_name = 'movie'


class RateMovieView(LoginRequiredMixin, CreateView):
    form_class = RateMovieForm
    success_url = reverse_lazy('movies:list')
    success_message = "You are rated this movie"
    template_name = 'movies/rate.html'
