from movies.models import Rate, Movie
from django import forms


class RateMovieForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rate
        fields = ("user", "movie", "stars")
