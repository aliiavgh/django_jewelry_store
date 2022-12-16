from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.account.tasks import send_activation_email, send_password_confirmation_email

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, required=True, write_only=True, )

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password_confirm')
        if p1 != p2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs

    @staticmethod
    def validate_email(email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('The user with this email already exists!')
        return email

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        send_activation_email.delay(user.email, user.activation_code)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')
        if p1 != p2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs

    def validate_old_password(self, old_password):
        user = self.context.get('user')
        if not user.check_password(old_password):
            raise serializers.ValidationError('Invalid password!')
        return old_password

    def set_new_password(self):
        user = self.context.get('user')
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    @staticmethod
    def validate_email(email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('The user with this email does not exist!')
        return email

    def send_activation_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_password_confirmation_email.delay(email, user.activation_code)


class ForgotPasswordConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    @staticmethod
    def validate_email(email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('The user with this email does not exist!')
        return email

    @staticmethod
    def validate_code(code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Invalid code!')
        return code

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')
        if p1 != p2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('new_password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()
