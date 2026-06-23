"""
WSGI config for blogicum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogicum.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73

application = get_wsgi_application()
