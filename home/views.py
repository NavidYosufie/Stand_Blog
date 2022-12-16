from django.shortcuts import render
from blog.models import Article


def home(request):
    articles = Article.objects.all().order_by("-created")[:3]
    articles_nav = Article.objects.all()[:4]
    return render(request, "home/index.html", {"article": articles, "articles_nav": articles_nav})



def sidenar(request):
    context = {"name": "navid"}
    return render(request, "includes/sidebar.html", context)





