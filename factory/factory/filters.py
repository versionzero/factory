import django_filters

from . import models


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = models.Product
        fields = {
            'name': ['contains', 'iexact', 'exact', 'iexact'],
            'description': ['contains', 'iexact', 'exact', 'iexact'],
            'price': ['lt', 'lte', 'exact', 'gt', 'gte'],
        }


class InventoryItemFilter(django_filters.FilterSet):

    class Meta:
        model = models.InventoryItem
        fields = {
            'quantity': ['lt', 'lte', 'exact', 'gt', 'gte']
        }
