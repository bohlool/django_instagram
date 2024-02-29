from django.db import models
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Follow, Profile
from .permissions import IsOwnerOrSuperuserOrReadonly, IsFollowerOrFollowedOrSuperuser
from .serializers import FollowSerializer, ProfileSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.none()
    serializer_class = FollowSerializer
    permission_classes = [IsFollowerOrFollowedOrSuperuser]

    def get_queryset(self):
        return Follow.objects.filter(models.Q(follower=self.request.user) | models.Q(following=self.request.user))


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.none()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
