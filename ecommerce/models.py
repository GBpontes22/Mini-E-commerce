"""Tabelas do mercadinho e calculos dos pedidos."""

from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Vendedor(models.Model):
    """Pessoa responsavel pelos produtos cadastrados."""

    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    """Produto com preco atual, estoque e vendedor responsavel."""

    # PROTECT impede apagar um vendedor que ainda possui produtos.
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome


class Cupom(models.Model):
    """Desconto opcional que pode ser associado a um pedido."""

    codigo = models.CharField(max_length=30, unique=True)
    desconto_percentual = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo


class Pedido(models.Model):
    """Agrupa os itens comprados e um possivel cupom de desconto."""

    criado_em = models.DateTimeField(auto_now_add=True)
    # Se o cupom for apagado, o pedido continua existindo.
    cupom = models.ForeignKey(Cupom, on_delete=models.SET_NULL, null=True, blank=True)

    def subtotal(self):
        """Soma os valores dos itens antes do desconto."""
        valor = Decimal("0.00")
        for item in self.itens.all():
            valor += item.subtotal()
        return valor

    def total(self):
        """Aplica o desconto do cupom ativo ao subtotal."""
        subtotal = self.subtotal()
        if self.cupom and self.cupom.ativo:
            desconto = subtotal * Decimal(self.cupom.desconto_percentual) / Decimal("100")
            return subtotal - desconto
        return subtotal

    def __str__(self):
        return f"Pedido #{self.id}"


class ItemPedido(models.Model):
    """Linha de um pedido: produto, quantidade e preco praticado."""

    # Apagar um pedido apaga seus itens; produtos usados em pedidos ficam protegidos.
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    # O preco fica gravado para que mudancas futuras no produto nao alterem pedidos antigos.
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def subtotal(self):
        """Calcula o valor desta linha do pedido."""
        return self.preco_unitario * self.quantidade

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
