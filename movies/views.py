from django.views.generic import ListView, DetailView, CreateView
from movies.models import Movie
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
    paginate_by = 8

    def get_queryset(self):
        print(f'COUNTRY 1>>> {self.request.GET.get("country")}')
        queryset = Movie.objects.all()
        if 'year' in self.request.GET:
            print(f'YEAR >>> {self.request.GET.get("year")}')
            return queryset.filter(year=self.request.GET.get('year'))
        elif 'genre' in self.request.GET:
            print(f'GENRE >>> {self.request.GET.get("genre")}')
            return queryset.filter(genre=self.request.GET.get('genre'))
        elif 'country' in self.request.GET:
            print(f'COUNTRY >>> {self.request.GET.get("country")}')
            return queryset.filter(country__name=self.request.GET.get('country'))
        else:
            print('USUAL >>> ')
            return queryset.order_by('-year')


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        # context['genres'] = [genre.title for genre in self.get_object().genre.all()]
        context['trailer_url'] = self.get_object().trailer_url + '?autoplay=1&mute=1'
        return context


class RateMovieView(LoginRequiredMixin, CreateView):
    form_class = RateMovieForm
    success_url = reverse_lazy('movies:list')
    success_message = "⭐ You are rated this movie"
    template_name = 'movies/rate.html'


class MyFormView(SuccessMessageMixin, FormView):
    template_name = 'movies/forms/my_form.html'
    form_class = MyForm
    success_url = reverse_lazy('core:home')
    success_message = "🟩 Form is successfully filled"
