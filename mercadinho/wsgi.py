"""Ponto de entrada WSGI usado por servidores compativeis com esse padrao."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mercadinho.settings")

# O servidor chama application para entregar requisicoes ao Django.
application = get_wsgi_application()
