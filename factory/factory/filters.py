import django_filters

from . import models


class InventoryItemFilter(django_filters.FilterSet):

    class Meta:
        model = models.InventoryItem
        fields = {
            'quantity': ['lt', 'lte', 'exact', 'gt', 'gte']
        }
