from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_desc = models.TextField(max_length=1000)
    product_stock = models.IntegerField()

    def __str__(self):
        return self.product_name
