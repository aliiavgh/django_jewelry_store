from rest_framework.routers import DefaultRouter

from applications.product.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = router.urls
