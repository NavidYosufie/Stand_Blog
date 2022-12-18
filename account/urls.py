from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path("register", views.register_user, name="register"),
    path("Login", views.login_user, name='login'),
    path("Logout", views.logout_user, name="logout"),
    path("edit", views.edit_user, name="edit"),
]