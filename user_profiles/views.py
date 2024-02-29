from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Follow, Profile
from .permissions import IsOwnerOrSuperuserOrReadonly, IsFollowingOrSuperuser, IsFollowerOrSuperuser
from .serializers import FollowRequestSerializer, ProfileSerializer, FollowResponseSerializer


class FollowingViewSet(mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Follow.objects.none()
    serializer_class = FollowRequestSerializer
    permission_classes = [IsFollowingOrSuperuser]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user.profile)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user.profile)


class FollowersViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Follow.objects.none()
    serializer_class = FollowResponseSerializer
    permission_classes = [IsFollowerOrSuperuser]

    def get_queryset(self):
        return Follow.objects.filter(followed=self.request.user.profile)


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
