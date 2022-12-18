from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("all-article", views.article_list, name="blog"),
    path("detail/<slug:slug>", views.post_detail, name="article_detail"),
    path("cateqory_detail/<slug:slug>", views.cateqory_detail, name="category_detail"),
    path("search/", views.search_article, name="search_articles"),
    path("contactus/", views.contactus, name="contact_us"),
    path("test", views.TestBaseView.as_view(), name="test"),
]