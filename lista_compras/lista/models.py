from django.db import models


class Item(models.Model):
    ITEM_STATUS = [
        ("ativo", "Ativo"),
        ("desativado", "Desativado")
    ]
    nome = models.CharField("Nome", max_length=100)
    quantidade = models.IntegerField("Quantidade")
    status = models.CharField("Status", default="ativo", choices=ITEM_STATUS, max_length=10)
