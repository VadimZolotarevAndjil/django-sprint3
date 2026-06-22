from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# на модель User можно сослатся
User = get_user_model()

class Blog(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(Blog):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True
    )

# тематическая категория
class Category(Blog):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField()

# Географическая метка
class Location(Blog):
    name = models.CharField(max_length=256)
