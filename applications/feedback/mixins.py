from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from applications.feedback.models import Like, Favorite, Rating
from applications.feedback.serializers import FavoriteSerializer, RatingSerializer


class LikeMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        like_obj, _ = Like.objects.get_or_create(product_id=pk, owner=request.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unliked'
        return Response({'status': status})


class FavoriteMixin:

    @action(detail=True, methods=['POST'])
    def add_to_favorites(self, request, pk=None):
        fav_obj, _ = Favorite.objects.get_or_create(product_id=pk, owner=request.user)
        fav_obj.favorite = not fav_obj.favorite
        fav_obj.save()
        status = 'in favorites'
        if not fav_obj.favorite:
            status = 'Removed from favorites'
        return Response({'status': status})


class RatingMixin:

    @action(detail=True, methods=['POST'])
    def rating(self, request, pk=None):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(product_id=pk, owner=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
