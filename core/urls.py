from rest_framework.routers import SimpleRouter

from core.views import *

router = SimpleRouter()
router.register(r'source', SourceViewSet)
router.register(r'status', StatusViewSet)
router.register(r'card', CardViewSet)
router.register(r'client', ClientViewSet)
router.register(r'manage', ManagerViewSet)
router.register(r'document', DocumentViewSet)
router.register(r'town-house', TownHouseViewSet)
router.register(r'construction', ConstructionViewSet)
router.register(r'locality', LocalityViewSet)
router.register(r'construction-stage', ConstructionStageViewSet)

urlpatterns = router.urls
