from rest_framework import viewsets
from rest_framework.response import Response

from .models import Post
from .permissions import IsOwnerOrSuperuserOrReadonly
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.none()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadonly]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
