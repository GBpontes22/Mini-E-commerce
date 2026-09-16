"""Enderecos do app ecommerce e views que respondem a cada um."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    # Listas e formularios de cadastro.
    path("vendedores/", views.vendedor_lista, name="vendedor_lista"),
    path("vendedores/novo/", views.vendedor_novo, name="vendedor_novo"),
    path("produtos/", views.produto_lista, name="produto_lista"),
    path("produtos/novo/", views.produto_novo, name="produto_novo"),
    path("produtos/<int:produto_id>/editar/", views.produto_editar, name="produto_editar"),
    # Fluxo de pedido: criar, consultar e adicionar itens.
    path("pedidos/", views.pedido_lista, name="pedido_lista"),
    path("pedidos/novo/", views.pedido_novo, name="pedido_novo"),
    path("pedidos/<int:pedido_id>/", views.pedido_detalhe, name="pedido_detalhe"),
    path("pedidos/<int:pedido_id>/itens/novo/", views.item_novo, name="item_novo"),
]
