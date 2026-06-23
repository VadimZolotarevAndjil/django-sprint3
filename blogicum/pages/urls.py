from django.urls import path
from pages import views

<<<<<<< HEAD
app_name = "pages"

urlpatterns = [
    path("about/", views.about, name="about"),
    path("rules/", views.rules, name="rules"),
=======
app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
]
