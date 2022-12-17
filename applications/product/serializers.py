from django.db.models import Avg
from rest_framework import serializers

from applications.product.models import Product, Image, Material


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(required=False)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES
        product = Product.objects.create(**validated_data)

        for image in files_data.getlist('images'):
            Image.objects.create(image=image, product=product)

        return product

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        images = [image['image'] for image in rep['images']]
        rep['images'] = images
        rep['likes'] = instance.likes.filter(like=True).count()
        rep['in favorites'] = instance.favorites.filter(favorite=True).count()
        rep['rating'] = instance.rating.all().aggregate(Avg('rating'))['rating__avg']
        rep['ordered products'] = instance.orders.filter(is_confirm=True).count()
        return rep


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if not instance.parent:
            rep.pop('parent')

        return rep
