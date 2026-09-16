"""Recebe requisicoes, consulta o banco e escolhe as paginas exibidas."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import ItemPedidoForm, ProdutoForm, VendedorForm
from .models import Pedido, Produto, Vendedor


def inicio(request):
    """Leva a pagina inicial para a lista de produtos."""
    return redirect("produto_lista")


def vendedor_lista(request):
    """Busca e mostra os vendedores cadastrados."""
    vendedores = Vendedor.objects.all()
    return render(request, "ecommerce/vendedor_lista.html", {"vendedores": vendedores})


def vendedor_novo(request):
    """Mostra o formulario e salva um vendedor enviado por POST."""
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendedor_lista")
    else:
        form = VendedorForm()
    return render(request, "ecommerce/form.html", {"form": form, "titulo": "Novo vendedor"})


def produto_lista(request):
    """Lista os produtos cadastrados."""
    produtos = Produto.objects.all()
    return render(request, "ecommerce/produto_lista.html", {"produtos": produtos})


def produto_novo(request):
    """Mostra o formulario e salva um produto enviado por POST."""
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("produto_lista")
    else:
        form = ProdutoForm()
    return render(request, "ecommerce/form.html", {"form": form, "titulo": "Novo produto"})


def pedido_lista(request):
    """Lista os pedidos cadastrados e seus totais."""
    pedidos = Pedido.objects.all()
    return render(request, "ecommerce/pedido_lista.html", {"pedidos": pedidos})


def pedido_novo(request):
    """Cria um pedido vazio; os itens sao adicionados depois."""
    if request.method == "POST":
        pedido = Pedido.objects.create()
        return redirect("pedido_detalhe", pedido_id=pedido.id)
    return render(request, "ecommerce/pedido_novo.html")


def pedido_detalhe(request, pedido_id):
    """Mostra itens, subtotais e total de um pedido existente."""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, "ecommerce/pedido_detalhe.html", {"pedido": pedido})


def item_novo(request, pedido_id):
    """Adiciona um item ao pedido e reduz o estoque do produto."""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == "POST":
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            # Completa os campos que nao aparecem no formulario antes de salvar.
            item = form.save(commit=False)
            item.pedido = pedido
            item.preco_unitario = item.produto.preco
            # A quantidade ja foi comparada com o estoque no ItemPedidoForm.
            item.produto.estoque -= item.quantidade
            item.produto.save()
            item.save()
            return redirect("pedido_detalhe", pedido_id=pedido.id)
    else:
        form = ItemPedidoForm()
    return render(request, "ecommerce/form.html", {"form": form, "titulo": "Adicionar item"})
