from rest_framework.routers import DefaultRouter

from applications.mailing.views import SpamViewSet

router = DefaultRouter()
router.register('', SpamViewSet)

urlpatterns = router.urls
