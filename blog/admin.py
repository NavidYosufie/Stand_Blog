from django.contrib import admin
from .models import Article, Cateqory, Comment

admin.site.register(Article)
admin.site.register(Cateqory)
admin.site.register(Comment)