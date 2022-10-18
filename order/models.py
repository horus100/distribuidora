from django.db import models
from product.models import Product
from user.models import Customer, User

# Create your models here.
class OrderPaper(models.Model):
    """ Clase abstracta de los para cada tipo de modelo DB"""
    discount = models.FloatField()
    subtotal = models.FloatField()
    igv = models.FloatField()
    total = models.FloatField()
    class Meta:
        abstract = True

class OrderDetail(models.Model):
    """ Clase abstracta para cada tipo de modelo detalle DB"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Id foraneo para obtener el nombre y precio del producto
    qty=models.IntegerField() #Cantidad del producto
    discount = models.SmallIntegerField() # Registra el descuento obtenido
    pricesale = models.FloatField() # Precio de venta despues del descuentp
    amount = models.FloatField()
    class Meta:
        abstract = True

class Order(models.Model):
    code= models.CharField(max_length=10)
    date= models.DateField(auto_now_add=True)
    time= models.TimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.code

class Sale(OrderPaper):
    """ Venta realizada, etapa 1"""
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class SaleDetail(OrderDetail):
    """ Detalle de la venta realizada"""
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE)


class Dispatch(OrderPaper):
    """ Despacho segun la venta realizada, etapa 2"""
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE)
    worker = models.ForeignKey(User,on_delete=models.CASCADE)

class DispatchDetail(OrderDetail):
    """ Detalle del despacho realizado"""
    dispatch = models.ForeignKey(Dispatch,on_delete=models.CASCADE)


class Accepted(OrderPaper):
    """ Productos aceptados etapa 3"""
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    dispatch = models.ForeignKey(Dispatch,on_delete=models.CASCADE)
    worker = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class AcceptedDetail(OrderDetail):
    """ Detalle de los productos aceptados"""
    accepted = models.ForeignKey(Accepted,on_delete=models.CASCADE)


class Rejected(OrderPaper):
    """ Productos devueltos etapa 3"""
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    dispatch = models.ForeignKey(Dispatch,on_delete=models.CASCADE)
    worker = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class RejectedDetail(OrderDetail):
    """ Detalle de los productos devueltos"""
    rejected = models.ForeignKey(Rejected,on_delete=models.CASCADE)

