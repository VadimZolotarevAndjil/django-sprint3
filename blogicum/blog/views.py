from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


from blog.models import Post, Category



def get_published_posts(category=None):
    qs = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
    ).select_related("author")
    if category:
        qs = qs.filter(category=category)
    return qs


def index(request):
    post_list = get_published_posts()
    return render(request, "blog/index.html", {"post_list": post_list})


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.select_related("category", "author"),
        id=pk,
        is_published=True
    )
    return render(request, "blog/detail.html", {"post": post})


def category(request, category_slug):
    template = "blog/category.html"
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    post_list = get_published_posts(category=category)
    context = {
        "category": category,
        "post_list": post_list,
    }
    return render(request, template, context)

