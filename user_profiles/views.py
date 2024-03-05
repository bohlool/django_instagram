from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from content.serializers import StorySerializer, PostSerializer
from view_log.mixins import TrackingRetrieveModelMixin
from .models import Follow, Profile
from .permissions import IsOwnerOrSuperuserOrReadonly, IsFollowingOrSuperuser, IsFollowerOrSuperuser, \
    IsOwnerOrSuperuserOrPublicProfileOrFollowingReadonly
from .serializers import FollowRequestSerializer, ProfileSerializer, FollowResponseSerializer, RegisterSerializer, \
    ChangePasswordSerializer, ChangeAccountSerializer


class RegisterViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = []


class FollowingViewSet(mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = FollowRequestSerializer
    permission_classes = [IsFollowingOrSuperuser]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class FollowersViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = FollowResponseSerializer
    permission_classes = [IsFollowerOrSuperuser]

    def get_queryset(self):
        return Follow.objects.filter(followed=self.request.user)


class ProfileViewSet(TrackingRetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    @action(detail=True, methods=['GET'], permission_classes=[IsOwnerOrSuperuserOrPublicProfileOrFollowingReadonly])
    def posts(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response(PostSerializer(profile.get_posts(), many=True).data)

    @action(detail=True, methods=['GET'], permission_classes=[IsOwnerOrSuperuserOrPublicProfileOrFollowingReadonly])
    def stories(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response(StorySerializer(profile.get_stories(), many=True).data)

    @action(detail=True, methods=['GET'], permission_classes=[IsOwnerOrSuperuserOrPublicProfileOrFollowingReadonly])
    def following(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response(FollowResponseSerializer(profile.get_following(), many=True).data)

    @action(detail=True, methods=['GET'], permission_classes=[IsOwnerOrSuperuserOrPublicProfileOrFollowingReadonly])
    def followers(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response(FollowResponseSerializer(profile.get_followers(), many=True).data)


class ChangePasswordViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangeAccountViewSet(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = ChangeAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
