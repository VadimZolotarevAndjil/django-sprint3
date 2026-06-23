from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related('author').filter(
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog\detail.html'
    post = get_object_or_404(
        Post.objects.filter(pk=pk, is_published=True)
    )
    context = {
        'post': post,
    }
    return render(request, template, context)


def category(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug)
    post_list = Post.objects.filter(category=category, is_published=True).select_related('category')
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
