from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()



