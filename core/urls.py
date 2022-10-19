from django.contrib import admin
from django.urls import path, include
from core.router import router

# importo registros de las urls de los viewSets
import order.urls
import product.urls
import road.urls
import units.urls
import user.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
