#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
<<<<<<< HEAD

=======
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogicum.settings")
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    main()
