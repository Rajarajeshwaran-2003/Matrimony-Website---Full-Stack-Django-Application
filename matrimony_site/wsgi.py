"""
WSGI config for matrimony_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the settings module for this WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matrimony_site.settings')

# Get the WSGI application
application = get_wsgi_application()
