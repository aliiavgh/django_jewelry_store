from django.contrib.auth import get_user_model
from django.db import models

from applications.product.models import Product

User = get_user_model()


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} - {self.like}'


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} - {self.product}'


class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='favorites')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} - {self.is_favorite}'


class Rating(models.Model):
    CHOICES = (
        (1, 'Bad'),
        (2, 'Ok'),
        (3, 'Fine'),
        (4, 'Good'),
        (5, 'Amazing')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    rating = models.SmallIntegerField(choices=CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.owner} - {self.rating}'