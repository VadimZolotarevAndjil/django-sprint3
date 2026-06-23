import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogicum.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73

application = get_asgi_application()
