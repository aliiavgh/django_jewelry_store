from rest_framework import serializers

from applications.mailing.models import Spam


class SpamSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = Spam
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        spam = Spam.objects.create(email=request.user)

        return spam

