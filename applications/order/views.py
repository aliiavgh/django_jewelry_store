from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from applications.order.models import Order
from applications.order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(consumer=self.request.user)


class OrderConfirmApiView(APIView):

    @staticmethod
    def get(request, confirmation_code):
        order = get_object_or_404(Order, confirmation_code=confirmation_code)
        order.is_confirm = True
        order.confirmation_code = ''
        order.save()
        return Response({'message': 'Your order successfully confirmed!'}, status=status.HTTP_200_OK)
