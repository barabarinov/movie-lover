from django.urls import path
from .views import DirectorDetailView, ActorDetailView

app_name = 'crew'

urlpatterns = [
    path('director/<int:pk>/', DirectorDetailView.as_view(), name='director'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor'),
]
