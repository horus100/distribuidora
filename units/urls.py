from core.router import router
from units.views import UmeasureViewSet, UmoneyViewSet

router.register('umeasure',UmeasureViewSet)
router.register('umoney', UmoneyViewSet)