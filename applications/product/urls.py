from rest_framework.routers import DefaultRouter

from applications.product.views import ProductViewSet, MaterialViewSet

router = DefaultRouter()
router.register('', ProductViewSet)
router.register('material', MaterialViewSet)

urlpatterns = router.urls
