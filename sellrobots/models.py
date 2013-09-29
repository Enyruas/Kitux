from django.db import models

# Create your models here.

class order(models.Model):
    item_id = models.IntegerField(default=0)
    product = models.CharField(max_length=200)
    brandName = models.CharField(max_length=200)

class useraccount(models.Model):
    username = models.EmailField(max_length=200)
    password = models.TextField(max_length=16)
