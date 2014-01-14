"""
WSGI config for homesite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os

# PROJECT_ENV_TYPE is one of (dev, prod, test), like settings or requirements file name
PROJECT_ENV_TYPE = os.environ['PROJECT_ENV_TYPE']
print 'running with PROJECT_ENV_TYPE=%s' % PROJECT_ENV_TYPE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % PROJECT_ENV_TYPE)

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
