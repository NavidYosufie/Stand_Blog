from django.shortcuts import render
from blog.models import Article


def home(request):
    articles = Article.custom_manager.all()
    return render(request, "home/index.html", {"article": articles})



def sidenar(request):
    context = {"name": "navid"}
    return render(request, "includes/sidebar.html", context)





