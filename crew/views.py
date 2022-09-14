from django.urls import reverse_lazy
from django.views.generic import DetailView
from crew.models import Director, Actor
from django.contrib.auth.mixins import LoginRequiredMixin


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'crew/director.html'
    context_object_name = 'director'


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'crew/actor.html'
    context_object_name = 'actor'


