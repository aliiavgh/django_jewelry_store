from rest_framework.routers import DefaultRouter

from applications.feedback.views import ReviewViewSet
from applications.product.views import ProductViewSet, MaterialViewSet

router = DefaultRouter()

router.register('material', MaterialViewSet)
router.register('reviews', ReviewViewSet)
router.register('', ProductViewSet)

urlpatterns = router.urls
