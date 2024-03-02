from django.db import models

from view_log.viewsets import TrackingModelViewSet
from .models import Post, Story
from .permissions import IsOwnerOrSuperuserOrReadonly
from .serializers import PostSerializer, StorySerializer


class PostViewSet(TrackingModelViewSet):
    queryset = Post.objects.none()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        return Post.objects.filter(
            models.Q(user=self.request.user) | models.Q(user__in=self.request.user.following.all()))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryViewSet(TrackingModelViewSet):
    queryset = Story.objects.none()
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        return Story.objects.filter(
            models.Q(user=self.request.user) | models.Q(user__in=self.request.user.following.all()))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
