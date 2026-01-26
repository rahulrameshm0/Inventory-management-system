from django.db import models
from django.contrib.auth.models import User
from add_products.models import Products

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'products')

    def __str__(self):
        return f"{self.user}"