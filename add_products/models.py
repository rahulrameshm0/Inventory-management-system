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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_types = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    vendor_name = models.CharField(max_length=150, blank=False)
    image = models.ImageField(upload_to='products/',blank=True, null=True)

    stripe_customer_id = models.CharField(max_length=255)
    stripe_checkout_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_product_id = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product_id) 