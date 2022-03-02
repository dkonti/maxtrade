from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0000)
    usd = models.FloatField(default=0.0000)
    btc = models.FloatField(default=0.0000)
    eth = models.FloatField(default=0.0000)
    
    def __str__(self):
        return str(self.user)