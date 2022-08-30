from django.views.generic import ListView, DetailView, CreateView
from movies.models import Movie, Rate
from movies.forms import RateMovieForm, MyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


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

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['genres'] = [genre.title for genre in self.get_object().genre.all()]
        return context


class RateMovieView(LoginRequiredMixin, CreateView):
    form_class = RateMovieForm
    success_url = reverse_lazy('movies:list')
    success_message = "You are rated this movie"
    template_name = 'movies/rate.html'


class MyFormView(SuccessMessageMixin, FormView):
    template_name = 'movies/forms/my_form.html'
    form_class = MyForm
    success_url = reverse_lazy('core:home')
    success_message = "🟩 Form is successfully filled"
