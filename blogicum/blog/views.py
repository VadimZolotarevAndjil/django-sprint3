<<<<<<< HEAD
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
=======
from django.shortcuts import get_object_or_404, render
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73

from blog.models import Post, Category


<<<<<<< HEAD

def index(request):
    template = "blog/index.html"
    post_list = (
        Post.objects.select_related("author")
        .filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
        )
        .order_by("-pub_date")[:5]
    )
    context = {
        "post_list": post_list,
=======
def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related('author').filter(
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')
    context = {
        'post_list': post_list,
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    }
    return render(request, template, context)


<<<<<<< HEAD

def post_detail(request, pk):
    template = "blog/detail.html"
    post = get_object_or_404(
        Post.objects.select_related("category").filter(
            pk=pk,
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
        )
    )
    context = {
        "post": post,
=======
def post_detail(request, pk):
    template = 'blog\detail.html'
    post = get_object_or_404(
        Post.objects.filter(pk=pk, is_published=True)
    )
    context = {
        'post': post,
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    }
    return render(request, template, context)


<<<<<<< HEAD

def category(request, category_slug):
    template = "blog/category.html"
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404("Категория не найдена")
    post_list = Post.objects.filter(
        category=category, is_published=True, pub_date__lte=timezone.now()
    ).select_related(
        "author"
    )
    context = {
        "category": category,
        "post_list": post_list,
=======
def category(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug)
    post_list = Post.objects.filter(category=category, is_published=True).select_related('category')
    context = {
        'category': category,
        'post_list': post_list,
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    }
    return render(request, template, context)
