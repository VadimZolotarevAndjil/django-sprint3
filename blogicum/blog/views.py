from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


from blog.models import Post, Category

def get_published_posts(pk):
    posts = Post.objects.all()
    posts = posts.filter(
            pk=pk,
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
    filtered_posts = get_published_posts()
    post = filtered_posts.select_related("category")
    context = {
        "post": post,
    }
    get_object_or_404(Post, id=pk, is_published=True)
    return render(request, template, context)


def category(request, category_slug):
    template = "blog/category.html"
    filtered_posts = get_published_posts(slug=category_slug)
    if not category.is_published:
        raise Http404("Категория не найдена")
    post_list = filtered_posts.objects.select_related(
        "author"
    )
    context = {
        "category": category,
        "post_list": post_list,
    }
    return render(request, template, context)
