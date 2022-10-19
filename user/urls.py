from core.router import router
from user.views import CustomerCategoryViewSet, CustomerViewSet, LocationViewSet, UserViewSet

router.register('user',UserViewSet)
router.register('location',LocationViewSet)
router.register('customer-category',CustomerCategoryViewSet)
router.register('customer',CustomerViewSet)