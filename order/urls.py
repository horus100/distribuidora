
from core.router import router

from order.views import AcceptedDetailViewSet, AcceptedViewSet, DispatchDetailViewSet, DispatchViewSet, OrderViewSet, RejectedDetailViewSet, RejectedViewSet, SaleDetailViewSet, SaleViewSet


router.register('order',OrderViewSet, basename='order')
router.register('sale',SaleViewSet)
router.register('sale-detail',SaleDetailViewSet)
router.register('dispatch',DispatchViewSet)
router.register('dispatch-detail',DispatchDetailViewSet)
router.register('accepted',AcceptedViewSet)
router.register('accepted-detail',AcceptedDetailViewSet)
router.register('rejected',RejectedViewSet)
router.register('rejected-detail',RejectedDetailViewSet)

