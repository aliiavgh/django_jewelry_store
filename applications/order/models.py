from django.contrib.auth import get_user_model
from django.db import models

from applications.product.models import Product

User = get_user_model()


class Order(models.Model):
    consumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    city = models.CharField(max_length=180)
    confirmation_code = models.CharField(max_length=180, blank=True)
    is_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.consumer} - {self.product} - {self.is_confirm}'

    def get_cost(self):
        return self.quantity * self.product.price

    def create_order_confirmation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.confirmation_code = code


