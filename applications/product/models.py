from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Material(models.Model):
    name = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name


class Product(models.Model):
    CHOICES = (
        ('1', 'In stock'),
        ('0', 'Out of stock')
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='products')
    status = models.CharField(max_length=100, choices=CHOICES)
    price = models.DecimalField(default=0, max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

