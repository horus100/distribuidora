from django.contrib import admin

from user.models import Customer, CustomerCategory, Location, User

# Register your models here.

admin.site.register(User)
admin.site.register(Location)
admin.site.register(CustomerCategory)
admin.site.register(Customer)