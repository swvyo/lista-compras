from rest_framework import serializers
from lista_compras.lista.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("__all__")
