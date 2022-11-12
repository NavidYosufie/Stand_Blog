from django.shortcuts import render, get_object_or_404
from blog.models import Article, Cateqory, Comment
from django.core.paginator import Paginator


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get("body")
        parent_id = request.POST.get("parent_id")
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    return render(request, "blog/article_detail.html", {"article": article})


def article_list(request):
    articles = Article.objects.filter(status=True)
    page_number = request.GET.get("page")
    paginator = Paginator(articles, 4)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"article": objects_list})


def cateqory_detail(request, slug):
    cateqory = get_object_or_404(Cateqory, slug=slug)
    articles = cateqory.articles.all()
    return render(request, "blog/article_list.html", {"article": articles})


def search_article(request):
    search = request.GET.get("search")
    article = Article.objects.filter(title__icontains=search)
    page_number = request.GET.get("page")
    paginator = Paginator(article, 1)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"article": object_list})
