from django.db import models


# Create your models here.

class Umeasure (models.Model): 
    """ Unidad de medida del producto"""
    name = models.CharField(max_length=255)

class Umoney (models.Model):
    """ Divisas """
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)