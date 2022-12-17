from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.order.views import OrderViewSet, OrderConfirmApiView


router = DefaultRouter()
router.register('', OrderViewSet)


urlpatterns = [
    path('confirm/<uuid:confirmation_code>/', OrderConfirmApiView.as_view())
] + router.urls
