from rest_framework.permissions import BasePermission


class IsReviewOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    @staticmethod
    def get_object_permission(request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            return request.user.is_authenticated and request.user == obj.owner
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)
