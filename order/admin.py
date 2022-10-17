from django.contrib import admin
from django.contrib.admin import AdminSite

from order.models import Order, OrderDetail, OrderPaper


# Register your models here
admin.site.register(Order)
admin.site.register(OrderPaper)
admin.site.register(OrderDetail)