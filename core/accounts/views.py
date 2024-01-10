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
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
class CustomLogoutView(LogoutView):
    success_url = reverse_lazy('song:home')