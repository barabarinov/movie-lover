from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_django_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm

User = get_user_model()


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegisterForm
    success_message = "🟩 Registration successful"


class LoginView(SuccessMessageMixin, auth_django_views.LoginView):
    template_name = 'accounts/login.html'
    success_message = "🟩 You have successfully logged in"

    def get_redirect_url(self):
        return super().get_redirect_url() or reverse('core:home')


class LogoutView(auth_django_views.LogoutView):

    def get_next_page(self):
        messages.info(self.request, "You have successfully logged out")
        return reverse('core:home')
