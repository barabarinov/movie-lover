from django.urls import path
from .views import DirectorDetailView

app_name = 'crew'

urlpatterns = [
    path('director/<int:pk>', DirectorDetailView.as_view(), name='director'),
]