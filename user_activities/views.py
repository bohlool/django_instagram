from rest_framework import viewsets

from .models import Like, Comment
from .permissions import IsOwnerOrSuperuserOrReadonly
from .serializers import LikeSerializer, CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
