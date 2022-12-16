from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.account.tasks import send_activation_email

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, required=True, write_only=True, )

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs['password_confirm']
        if p1 != p2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs

    def validate_email(self, email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError('User with this email already exists!')
        return email

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        send_activation_email.delay(user.email, user.activation_code)
        return user
