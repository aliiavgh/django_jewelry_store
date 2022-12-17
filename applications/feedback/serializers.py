from rest_framework import serializers

from applications.feedback.models import Like, Review, Favorite, Rating
from applications.product.serializers import ProductSerializer


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Review
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('product', )


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('rating', )
