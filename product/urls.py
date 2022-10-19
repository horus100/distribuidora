from django.urls import path,include
from core.router import router
from product.views import CategoryViewSet, ProductViewSet

router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
