from core.router import router
from road.views import RoadCargoViewSet, RoadMapViewSet, RoadViewSet

router.register('road', RoadViewSet)
router.register('roadmap', RoadMapViewSet)
router.register('roadcargo', RoadCargoViewSet)