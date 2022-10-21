from django.contrib import admin
from django.urls import path, include
from core.router import router

# importo registros de las urls de los viewSets
import order.urls
import product.urls
import road.urls
import units.urls
import user.urls

#JWT auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('rest_registration.api.urls')),
    path('accounts/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
