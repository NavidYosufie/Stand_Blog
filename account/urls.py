from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path("register", views.user_register, name="register"),
    path("Login", views.user_login, name='login'),
    path("Logout", views.user_logout, name="logout")
]