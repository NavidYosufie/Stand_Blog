from django.shortcuts import render
from blog.models import Article
from django.views.generic import View
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Article.objects.all()[:4]
        return context





