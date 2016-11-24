from rest_framework import serializers

from . import models


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = ('name', 'description', 'price')


class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InventoryItem
        fields = ('product', 'quantity')
