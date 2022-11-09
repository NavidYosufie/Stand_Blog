from django.shortcuts import render, get_object_or_404
from blog.models import Article, Cateqory
from django.core.paginator import Paginator


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/post-details.html", {"article": article})



def article_list(request):
    articles = Article.objects.filter(status=True)
    page_number = request.GET.get("page")
    paginator = Paginator(articles, 4)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/blog.html", {"article": objects_list})


def cateqory_detail(request, slug):
    cateqory = get_object_or_404(Cateqory, slug=slug)
    articles = cateqory.articles.all()
    return render(request, "blog/blog.html", {"article": articles})
