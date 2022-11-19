from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Cateqory(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    

    def get_absolut_url(self):
        return reverse("blog:category_detail", kwargs={"slug": self.slug})

    def save(self):
        self.slug = slugify(self.title)
        super(Cateqory, self).save()

    def __str__(self) -> str:
        return self.title


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

    def content(self):
        return len(self.all())

    def puplisi(self):
        return self.filter(status=True)

    def get_title(self):
        return self.filter(title="python")



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cateqory = models.ManyToManyField(Cateqory, blank=True, related_name="articles")
    title = models.CharField(max_length=90)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="image/article")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    myfile = models.FileField(upload_to="file", null=True, blank=True)
    status = models.BooleanField(null=True, blank=True, default=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    objects = models.Manager()
    custom_manager = ArticleManager()

    class Meta:
        verbose_name = "post"

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return f"{self.title}  -   {self.body[:20]}"



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.body[:50]



class Massege(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    created_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title