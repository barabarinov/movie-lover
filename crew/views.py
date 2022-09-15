from django.views.generic import DetailView
from crew.models import Director, Actor


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'crew/director.html'
    context_object_name = 'director'


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'crew/actor.html'
    context_object_name = 'actor'
