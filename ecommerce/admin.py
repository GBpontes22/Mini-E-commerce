"""Cadastros disponiveis no painel administrativo interno do Django."""

from django.contrib import admin

from .models import Cupom, ItemPedido, Pedido, Produto, Vendedor


class ItemPedidoInline(admin.TabularInline):
    """Exibe os itens dentro da pagina administrativa do pedido."""

    model = ItemPedido
    extra = 0


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    """Mostra dados basicos e itens de cada pedido no painel."""

    list_display = ("id", "criado_em", "cupom")
    inlines = [ItemPedidoInline]


# Estes tres models tambem podem ser gerenciados no painel interno.
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Cupom)
