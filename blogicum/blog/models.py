<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.db import models

=======
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# на модель User можно сослатся
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
User = get_user_model()

class Blog(models.Model):
    is_published = models.BooleanField(
        default=True,
<<<<<<< HEAD
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Добавлено"
=======
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    )

    class Meta:
        abstract = True

<<<<<<< HEAD

class Post(Blog):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок"
    )
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — "
            "можно делать отложенные публикации."
        ),
=======
class Post(Blog):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем ' \
        '— можно делать отложенные публикации.'
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
<<<<<<< HEAD
        verbose_name="Автор публикации"
    )
    location = models.ForeignKey(
        "Location",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Местоположение"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория"
    )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title

# Тематическая категория
class Category(Blog):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок"
    )
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(
        blank=False,
        unique=True,
        verbose_name="Идентификатор",
        help_text=(
            "Идентификатор страницы для URL; "
            "разрешены символы латиницы, цифры, дефис и подчёркивание."
        )
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

# Географическая метка
class Location(Blog):
    name = models.CharField(
        max_length=256,
        verbose_name="Название места"
    )

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

=======
        verbose_name='Автор'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
    
    def __str__(self):
        return self.title 

# тематическая категория
class Category(Blog):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        blank=False,
        verbose_name='Индификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.title 

# Географическая метка
class Location(Blog):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
    
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    def __str__(self):
        return self.name
