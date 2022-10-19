from django.contrib import admin
from django.urls import path, include
from core.router import router

import order.urls
import product.urls
import road.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
