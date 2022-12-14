import datetime

from movies.models import Rate, Movie
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class RateMovieForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rate
        fields = ("user", "movie", "stars")


class MyForm(forms.Form):
    fav_movie = forms.CharField(label='Favorite Movies', required=False, initial=None)
    fav_actor = forms.CharField(label='Favorite Actors', initial=None)
    fav_director = forms.CharField(label='Favorite Director', initial=None)
    date_field = forms.DateField(label='Birthday',
                                 widget=forms.SelectDateWidget(years=range(datetime.datetime.now().year, 1944, -1)))
    int_field = forms.IntegerField(label='Favorite Number', initial=None)
    email_field = forms.EmailField(label='Email',
                                   initial=None)

    password = forms.CharField(max_length=20,
                               min_length=8,
                               widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[('1', 'man'), ('2', 'woman')])
    bool_field = forms.BooleanField(label='Remember Me',
                                    required=False,
                                    help_text="* after that you don't need to login again")
