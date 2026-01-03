from django.db import models

class Products(models.Model):
    PRODUCT_STATUS = [
        ('IN STOCK', 'In stock'),
        ('OUT OF STOCK', 'Out of stock'),
    ]

    PRODUCT_TYPES = [
        ('electronics', 'Electronics'),
        ('grocery', 'Grocery'),
        ('clothing', 'Clothing'),
    ]
    product_id = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20,choices=PRODUCT_STATUS)
    product_types = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    vendor_name = models.CharField(max_length=150)


