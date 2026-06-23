from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
=======

from django.urls import include, path

>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
from django.conf import settings


urlpatterns = [
<<<<<<< HEAD
    path("", include("blog.urls", namespace="blog")),
    path("admin/", admin.site.urls),
    path("pages/", include("pages.urls")),
=======
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
]

if settings.DEBUG:
    import debug_toolbar
<<<<<<< HEAD
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
=======
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),) 
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
