from django.urls import path
from movies.views import MovieDetailView
from .views import DirectorDetailView

app_name = 'crew'

urlpatterns = [
    path('', MovieDetailView.as_view(), name='detail'),
    path('<int:pk>/director/', DirectorDetailView.as_view(), name='director_detail'),
]
