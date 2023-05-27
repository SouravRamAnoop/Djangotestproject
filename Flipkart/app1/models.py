from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    description=models.CharField(max_length=500)