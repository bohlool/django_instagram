from django.db import models
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from user_activities.models import Like, Comment
from user_activities.serializers import CommentSerializer, LikeSerializer
from user_profiles.models import Follow
from view_log.models import ViewLog
from view_log.serializers import ViewLogSerializer
from view_log.viewsets import TrackingModelViewSet
from .models import Post, Story
from .permissions import IsOwnerOrSuperuserOrReadonly
from .serializers import PostSerializer, StorySerializer


class PostViewSet(TrackingModelViewSet):
    queryset = Post.objects.none()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        following_users = Follow.objects.get_following(self.request.user).values_list('follower', flat=True)
        return Post.objects.filter(
            models.Q(user=self.request.user) | models.Q(user__in=following_users))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True)
    def views(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(ViewLogSerializer(post.get_views(), many=True).data)

    @action(detail=True, methods=['POST'])
    def do_like(self, request, *args, **kwargs):
        post = self.get_object()
        Like.objects.track_like(post, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def likes(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(LikeSerializer(post.get_likes(), many=True).data)

    @action(detail=True, methods=['POST'])
    def do_comment(self, request, *args, **kwargs):
        post = self.get_object()
        Comment.objects.create_comment(post, request.user, request.data.get('text'))
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def comments(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(CommentSerializer(post.get_comments(), many=True).data)


class StoryViewSet(TrackingModelViewSet):
    queryset = Story.objects.none()
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        following_users = Follow.objects.get_following(self.request.user).values_list('follower', flat=True)
        return Story.objects.filter(
            (models.Q(user=self.request.user) | models.Q(user__in=following_users)) & models.Q(is_active=True))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True)
    def views(self, request, *args, **kwargs):
        story = self.get_object()
        return Response(ViewLogSerializer(story.get_views(), many=True).data)

    @action(detail=True, methods=['POST'])
    def do_like(self, request, *args, **kwargs):
        story = self.get_object()
        Like.objects.track_like(story, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def likes(self, request, *args, **kwargs):
        story = self.get_object()
        return Response(LikeSerializer(story.get_likes(), many=True).data)
