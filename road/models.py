from django.db import models
from order.models import Dispatch
from user.models import Customer, User
# Create your models here.

class Road(models.Model):
    """ Modelo para crear una categoria ruta y asociarlo a un trabajador con 
        rol de transporte """
    name = models.CharField(max_length=50, unique=True) #Cada ruta debe tener un nombre unico
    transport = models.OneToOneField(User,on_delete=models.CASCADE,null=True) #Un usuario solo debe estar asignado a una ruta

class RoadMap(models.Model):
    """ Modelo para asociar las diferentes direcciones en un tipo de ruta en orden
        ascendente segun su cercania"""
    road = models.ForeignKey(Road,on_delete=models.CASCADE)
    address = models.ForeignKey(Customer,on_delete=models.CASCADE)
    orderlist = models.SmallIntegerField() # orden de lista segun la cercania

class RoadCargo(models.Model):
    """ Modelo que asociara la carga de despachos de cada cliente"""
    road = models.ForeignKey(Road,on_delete=models.CASCADE)
    dispatch = models.ForeignKey(Dispatch,on_delete=models.CASCADE)
    devoted = models.BooleanField(default=False)