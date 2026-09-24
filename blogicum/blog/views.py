from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


from blog.models import Post, Category

def get_published_posts():
    posts = Post.objects.all()
    posts = posts.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
        )
    return posts


def index(request):
    template = "blog/index.html"
    filtered_posts = get_published_posts()
    post_list = (
        filtered_posts.select_related("author")
    )
    context = {"post_list": post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = "blog/detail.html"
    post = get_object_or_404(
        Post.objects.select_related("category", "author"),
        id=pk,
        is_published=True
    )
    context = {"post": post}
    return render(request, template, context)


def category(request, category_slug):
    template = "blog/category.html"
    category = Category.objects.get(slug=category_slug)
    if not category.is_published:
        raise Http404("Категория не найдена")
    filtered_posts = get_published_posts()
    post_list = filtered_posts.filter(category=category).select_related("author")
    context = {
        "category": category,
        "post_list": post_list,
    }
    return render(request, template, context)

