from rest_framework.response import Response
from rest_framework.decorators import action

from applications.feedback.models import Like


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


