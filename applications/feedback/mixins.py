from rest_framework.response import Response
from rest_framework.decorators import action

from applications.feedback.models import Like, Favorite
from applications.feedback.serializers import FavoriteSerializer


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

