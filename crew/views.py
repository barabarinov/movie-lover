from django.urls import reverse_lazy
from django.views.generic import DetailView
from crew.models import Director
from django.contrib.auth.mixins import LoginRequiredMixin


class DirectorDetailView(DetailView):
    model = Director

    template_name = 'crew/director.html'
    context_object_name = 'director'
