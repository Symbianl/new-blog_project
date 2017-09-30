"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

sys.path.append('D:/python2.7/Scripts')
sys.path.append('D:/python2.7/Scripts/blog_project')
sys.path.append('D:/python2.7/Scripts/blog_project/blog')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")

application = get_wsgi_application()
