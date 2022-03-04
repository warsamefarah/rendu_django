"""
WSGI config for rendu_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from socketio_app.views import sio
from socketio import WSGIApp
import eventlet
import eventlet.wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rendu_django.settings')

application = get_wsgi_application()

application = WSGIApp(sio, application)

eventlet.wsgi.server(eventlet.listen(('', 8000)), application)

