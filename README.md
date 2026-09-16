# Mini E-commerce

Projeto escolhido da disciplina: **Mini E-commerce**.

## Objetivo

Sistema simples de pedido com multiplos itens, calculo de total e baixa de estoque.

## Entidades

- Produto
- Vendedor
- Pedido
- Item
- Cupom

## P1

Carrinho/pedido com calculo de total.

## Como rodar

```bash
cd mercadinho
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```
