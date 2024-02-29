from django.db import models
from rest_framework import viewsets

from .models import Message
from .permissions import IsOwnerOrSuperuserOrReadonly
from .serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.none()
    serializer_class = MessageSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(models.Q(sender=user) | models.Q(receiver=user)).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
