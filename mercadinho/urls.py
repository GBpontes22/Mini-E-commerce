"""Rotas gerais: inclui as paginas do ecommerce e o painel do Django."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # O app define os caminhos de produtos, vendedores e pedidos.
    path("", include("ecommerce.urls")),
    # Painel interno, sem link no menu principal do site.
    path("admin/", admin.site.urls),
]
