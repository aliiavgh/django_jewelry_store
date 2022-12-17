from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from applications.feedback.models import Review
from applications.feedback.permissions import IsReviewOwner
from applications.feedback.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
