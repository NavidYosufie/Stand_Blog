from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("all-article", views.article_list, name="blog"),
    path("about/", views.about, name="about"),
    path("detail/<slug:slug>", views.ArticleDetailView.as_view(), name="article_detail"),
    path("cateqory_detail/<slug:slug>", views.cateqory_detail, name="category_detail"),
    path("search/", views.search_article, name="search_articles"),
    path("contactus/", views.contactus, name="contact_us"),
    path("art/", views.ArticleList.as_view(), name="Aer"),
]