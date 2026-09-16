"""Ponto de entrada ASGI usado por servidores compativeis com esse padrao."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mercadinho.settings")

# O servidor chama application para entregar requisicoes ao Django.
application = get_asgi_application()
