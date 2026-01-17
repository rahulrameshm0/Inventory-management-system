from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings



class Products(models.Model):
    PRODUCT_STATUS = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'OUT of Stock'),
    ]

    PRODUCT_TYPES = [
        ('electronics', 'Electronics'),
        ('grocery', 'Grocery'),
        ('clothing', 'Clothing'),
        ('fitness', 'Fitness'),
        ('toys', 'Toys')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField(unique=True)
    quantity = models.CharField(max_length=150)
    status = models.CharField(max_length=20,choices=PRODUCT_STATUS)
    product_types = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    vendor_name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return str(self.product_id) 