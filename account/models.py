from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)

    def __str__(self):
        return str(self.username)
        