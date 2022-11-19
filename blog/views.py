from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Cateqory, Comment, Massege
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm

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
    get_number_page = request.GET.get("page")
    paginator = Paginator(article, 1)
    object_list = paginator.get_page(get_number_page)
    return render(request, "blog/article_list.html", {"article": object_list})



def contactus(request):
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            Massege.objects.create(title=title, email=email, message=message)
    else:
        form = MessageForm()
    return render(request, "blog/contact_us.html", {"form": form})
