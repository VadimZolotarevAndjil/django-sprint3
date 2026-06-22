from django.shortcuts import get_object_or_404, render

from django.http import Http404

from blog.models import Post



def index(request):
    template = 'blog\index.html'
    post_detail = Post.objects.values(
        'id',
        'title',
        'description'
    )
    context = {
        'post_detail': post_detail,
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog\detail.html'
    post_detail = get_object_or_404(
        Post.objects.values(
            'title',
            'description'
        ).filter(is_published=True),
        pk=pk
    )
    context = {
        'post_detail': post_detail,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog\category.html'
    
    context = {
        'post_detail': post_detail,
    }
    return render(request, template, context)
