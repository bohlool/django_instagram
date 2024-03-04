from django.db import models
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from user_activities.serializers import CommentSerializer
from user_activities.utils import get_comments, get_likes, track_like, create_comment
from view_log.utils import get_views
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

    @action(detail=True)
    def views(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(CommentSerializer(get_views(post), many=True).data)

    @action(detail=True, methods=['POST'])
    def do_like(self, request, *args, **kwargs):
        post = self.get_object()
        track_like(post, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def likes(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(CommentSerializer(get_likes(post), many=True).data)

    @action(detail=True, methods=['POST'])
    def do_comment(self, request, *args, **kwargs):
        post = self.get_object()
        create_comment(post, request.user, request.data.get('text'))
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def comments(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(CommentSerializer(get_comments(post), many=True).data)


class StoryViewSet(TrackingModelViewSet):
    queryset = Story.objects.none()
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        return Story.objects.filter(
            (models.Q(user=self.request.user) | models.Q(user__in=self.request.user.following.all())) & models.Q(
                is_active=True))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True)
    def views(self, request, *args, **kwargs):
        story = self.get_object()
        return Response(CommentSerializer(get_views(story), many=True).data)

    @action(detail=True, methods=['POST'])
    def do_like(self, request, *args, **kwargs):
        story = self.get_object()
        track_like(story, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def likes(self, request, *args, **kwargs):
        story = self.get_object()
        return Response(CommentSerializer(get_likes(story), many=True).data)
