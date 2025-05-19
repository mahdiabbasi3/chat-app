"""
ASGI config for djangoProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()
from channels.auth import AuthMiddlewareStack
import chat.routing
from chat.jwt_middlewere import jwtmiddleware
from channels.routing import ProtocolTypeRouter, URLRouter




application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":jwtmiddleware(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
