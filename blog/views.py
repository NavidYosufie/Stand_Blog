from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Cateqory, Comment, Messege
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

def category(request):
    category_detail = Cateqory.objects.all()
    return render(request, "blog/article_list.html", {"category": category_detail})

def cateqory_detail(request, slug):
    page_number = request.GET.get("page")
    cateqory = get_object_or_404(Cateqory, slug=slug)
    articles = cateqory.articles.all()
    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"article": object_list})


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
            instance = form.save(commit=False)
            instance.title = instance.title.upper()
            instance.save()

    else:
        form = MessageForm()
    return render(request, "blog/contact_us.html", {"form": form})
