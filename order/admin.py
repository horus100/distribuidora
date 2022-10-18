from django.contrib import admin

from order.models import Accepted, AcceptedDetail, Dispatch, DispatchDetail, Order,  Rejected, RejectedDetail, Sale, SaleDetail


# Register your models here
admin.site.register(Order)
admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.register(Dispatch)
admin.site.register(DispatchDetail)
admin.site.register(Accepted)
admin.site.register(AcceptedDetail)
admin.site.register(Rejected)
admin.site.register(RejectedDetail)