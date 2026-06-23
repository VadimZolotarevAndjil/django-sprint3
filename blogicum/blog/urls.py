from django.urls import path

from . import views

<<<<<<< HEAD
app_name = "blog"


urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("category/<slug:category_slug>/",
        views.category,
        name="category_posts"
=======

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', 
        views.category,
        name='category_posts'
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    ),
]
