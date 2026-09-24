from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from constants import PUBLICATION_DAYS

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
        .order_by("-pub_date")[:PUBLICATION_DAYS]
    )
    context = {"post_list": post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = "blog/detail.html"
    post = get_object_or_404(
         Post.objects.select_related("category").# filter(
        #     pk=pk,
        #     is_published=True,
        #     category__is_published=True,
        #     pub_date__lte=timezone.now(),
        # )
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
    post_list = Post.objects#.filter(
        # category=category, is_published=True, pub_date__lte=timezone.now()
    ).select_related(
        "author"
    )
    context = {
        "category": category,
        "post_list": post_list,
    }
    return render(request, template, context)

        # .filter(
        #     is_published=True,
        #     category__is_published=True,
        #     pub_date__lte=timezone.now(),
        # )
# filter(
        #     pk=pk,
        #     is_published=True,
        #     category__is_published=True,
        #     pub_date__lte=timezone.now(),
        # )

#.filter(
        # category=category, 
        # is_published=True,
        # pub_date__lte=timezone.now()
    # )