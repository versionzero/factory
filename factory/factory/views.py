import django_filters
from rest_framework import viewsets
from rest_framework import filters as rest_filters

from . import models
from . import serializers
from . import filters


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = models.Product.objects.all()
    filter_class = filters.ProductFilter
    serializer_class = serializers.ProductSerializer
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        rest_filters.SearchFilter,)
    search_fields = ('name', 'description')


class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items in the inventory to be viewed or edited.
    """
    queryset = models.InventoryItem.objects.all()
    filter_class = filters.InventoryItemFilter
    serializer_class = serializers.InventoryItemSerializer
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        rest_filters.SearchFilter,)
    search_fields = ('product__name', 'product__description')

