from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, UserEditForm


def user_register(request):
    if request.user.is_authenticated:
        return redirect("home:home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get("username"), email=form.cleaned_data.get("email"), password=form.cleaned_data.get("password_2"))
            login(request, user)
            return redirect("home:home")
    else:
        form = RegisterForm()
    return render(request, "account/register.html", {"form": form})


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

def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
    return render(request, "account/Edit.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home:home")

