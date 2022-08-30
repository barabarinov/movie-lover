import datetime

from movies.models import Rate, Movie
from django import forms


class RateMovieForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rate
        fields = ("user", "movie", "stars")


class MyForm(forms.Form):
    fav_movie = forms.CharField(label='Favorite Movie', required=False, initial='Matrix')
    fav_actor = forms.CharField(label='Favorite Actor', initial='Denzel Washington')
    fav_director = forms.CharField(label='Favorite Director', initial='Steven Spilberg')
    email_field = forms.EmailField(label='Email', initial='user@mail.com')
    date_field = forms.DateField(label='Birthday',
                                 widget=forms.SelectDateWidget(years=range(datetime.datetime.now().year, 1944, -1)))
    int_field = forms.IntegerField(label='Favorite Number', initial='0')
    password = forms.CharField(max_length=20,
                               min_length=8,
                               widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[('1', 'man'), ('2', 'woman')])
    bool_field = forms.BooleanField(label='Remember Me',
                                    required=False,
                                    help_text="* after that you don't need to login again")
