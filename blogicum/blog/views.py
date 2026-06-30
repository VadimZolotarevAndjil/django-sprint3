from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category



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
    }
    return render(request, template, context)



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
    }
    return render(request, template, context)



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
    }
    return render(request, template, context)
