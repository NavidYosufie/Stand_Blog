from blog.models import Article, Cateqory

def recent_articles(request):
    recent_articles = Article.objects.order_by("-created",)[:2]
    return {"recent_articles": recent_articles}


def cateqouries(request):
    cateqouries = Cateqory.objects.all()
    return {"cateqouries": cateqouries}