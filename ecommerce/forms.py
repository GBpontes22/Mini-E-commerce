"""Formularios gerados a partir dos models para as telas de cadastro."""

from django import forms

from .models import ItemPedido, Pedido, Produto, Vendedor


class VendedorForm(forms.ModelForm):
    """Recebe nome e email de um vendedor."""

    class Meta:
        model = Vendedor
        fields = ["nome", "email"]


class ProdutoForm(forms.ModelForm):
    """Recebe os dados necessarios para cadastrar um produto."""

    class Meta:
        model = Produto
        fields = ["vendedor", "nome", "preco", "estoque"]


class ProdutoEdicaoForm(forms.ModelForm):
    """Altera vendedor, nome do vendedor, preco e estoque."""

    novo_nome_vendedor = forms.CharField(
        label="Novo nome do vendedor (opcional)",
        max_length=120,
        required=False,
        help_text="A mudanca aparece em todos os produtos deste vendedor.",
    )

    class Meta:
        model = Produto
        fields = ["vendedor", "novo_nome_vendedor", "preco", "estoque"]
        labels = {"vendedor": "Vendedor"}


class PedidoForm(forms.ModelForm):
    """Cria um pedido com cupom opcional."""

    class Meta:
        model = Pedido
        fields = ["cupom"]


class ItemPedidoForm(forms.ModelForm):
    """Adiciona um produto e sua quantidade a um pedido."""

    class Meta:
        model = ItemPedido
        fields = ["produto", "quantidade"]

    def clean(self):
        """Impede pedir mais unidades do que ha no estoque."""
        dados = super().clean()
        produto = dados.get("produto")
        quantidade = dados.get("quantidade")
        if produto and quantidade and quantidade > produto.estoque:
            raise forms.ValidationError("Quantidade maior que o estoque disponivel.")
        return dados
