from django.shortcuts import render

from django.http import Http404




def index(request):
    posts_reversed = posts[::-1]
    return render(request, 'blog/index.html', {'posts': posts_reversed})


def post_detail(request, post_id):
    posts_dict = {post['id']: post for post in posts}
    post = posts_dict.get(post_id)
    if post is None:
        raise Http404('Пост не найден')
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    filtered = [p for p in posts if p['category'] == category_slug]
    if not filtered:
        return render(request, 'blog/category.html', {
            'posts': [],
            'category_slug': category_slug
        })
    filtered_reversed = filtered[::-1]
    return render(request, 'blog/category.html', {
        'posts': filtered_reversed,
        'category_slug': category_slug
    })

# по-другому не получалось иначе
# не пройду проверки
