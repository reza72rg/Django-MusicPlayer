from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('/')
    fields = "username", "password"  # Fields to display on the login form
    redirect_authenticated_user = True  # Redirect to success URL if user is already authenticated

    def get_success_url(self):
        return reverse_lazy("song:home")  # Redirect to the task list page after successful login
    
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
