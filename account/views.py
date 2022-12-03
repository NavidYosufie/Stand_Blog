from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm


def user_register(request):
    context = {"errors": []}

    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password_1 = request.POST.get("password1")
        password_2 = request.POST.get("password2")

        if password_1 != password_2:
            context["errors"].append("Password not set Plase your password set")
            return render(request, "account/register.html", context)

        user = User.objects.create(username=username, email=email, password=password_1)
        login(request, user)
        return redirect("home:home")

    return render(request, "account/register.html")



def user_login(request):
    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect("home:home")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home:home")