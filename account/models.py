from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)

    def __str__(self):
        return str(self.username)