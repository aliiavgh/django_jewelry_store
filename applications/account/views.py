from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, \
    ForgotPasswordConfirmSerializer

User = get_user_model()


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ActivationAPIView(APIView):

    @staticmethod
    def get(request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'message': 'Your account successfully activated!'}, status=status.HTTP_200_OK)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = ChangePasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Your password successfully changed!', status=status.HTTP_200_OK)


class ForgotPasswordAPIView(APIView):

    @staticmethod
    def post(request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid()
        serializer.send_activation_code()
        return Response('Check tour email, we have sent you a code to update your password', status=status.HTTP_200_OK)


class ForgotPasswordConfirmAPIView(APIView):

    @staticmethod
    def post(request):
        serializer = ForgotPasswordConfirmSerializer(data=request.data)
        serializer.is_valid()
        serializer.set_new_password()
        return Response('Your password successfully updated!', status=status.HTTP_200_OK)