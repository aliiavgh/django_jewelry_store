from rest_framework import serializers

from applications.order.models import Order
from applications.order.tasks import send_order_confirmation_email


class OrderSerializer(serializers.ModelSerializer):
    consumer = serializers.CharField(required=False)

    class Meta:
        model = Order
        exclude = ('confirmation_code', )

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.create_order_confirmation_code()
        order.save()
        send_order_confirmation_email.delay(order.consumer.email, order.confirmation_code)
        return order

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = instance.product.title
        rep['cost'] = instance.get_cost()
        return rep
