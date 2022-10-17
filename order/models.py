from django.db import models
from product.models import Product

# Create your models here.

class Order(models.Model):
    code= models.CharField(max_length=10)
    date= models.DateField(auto_now_add=True)
    time= models.TimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.code


class OrderPaper(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    discount = models.FloatField()
    subtotal = models.FloatField()
    igv = models.FloatField()
    total = models.FloatField()
    class Type(models.TextChoices):
        """Enumeracion de los tipos de estado de la orden """
        Pedido = "Pedido", "Pedido"
        Entrega = "Entrega", "Entrega"
        EntregaAceptada = "EntregaAceptada", "Entrega Aceptada"
        EntregaRechazada = "EntregaRechazada","Entrega Rechazada"
    type = models.CharField(max_length=20,choices=Type.choices,default=Type.Pedido)

    def __str__(self) -> str:
        return self.type

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Id foraneo para obtener el nombre y precio del producto
    qty=models.IntegerField() #Cantidad del producto
    discount = models.SmallIntegerField() # Registra el descuento obtenido
    pricesale = models.FloatField() # Precio de venta despues del descuentp
    amount = models.FloatField()
