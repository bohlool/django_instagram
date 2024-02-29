from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    view_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'caption', 'view_count', 'created', 'modified')
