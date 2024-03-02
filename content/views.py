from rest_framework import viewsets
from rest_framework.response import Response

from view_log.utils import track_view
from .models import Post
from .permissions import IsOwnerOrSuperuserOrReadonly
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.none()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        track_view(instance, self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
