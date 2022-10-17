from django.db import models

from units.models import Umeasure

# Create your models here.
class Category(models.Model):
    """ Categorias para productos"""
    name = models.CharField(max_length=255)

class Product(models.Model):
    """ Productos de la distribuidora"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_measure = models.ForeignKey(Umeasure, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()


