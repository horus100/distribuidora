from django.contrib import admin

from road.models import Road, RoadCargo, RoadMap

# Register your models here.
admin.site.register(Road)
admin.site.register(RoadMap)
admin.site.register(RoadCargo)