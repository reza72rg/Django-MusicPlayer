from django.urls import path, include
from accounts.views import UserRegisterView, UserLoginView, CustomLogoutView

app_name = "accounts"

urlpatterns = [
    # Task list view
    path("register/",UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]