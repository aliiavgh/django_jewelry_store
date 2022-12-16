from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer

User = get_user_model()


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ActivationAPIView(APIView):

    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'message': 'Your account successfully activated!'}, status=status.HTTP_200_OK)
