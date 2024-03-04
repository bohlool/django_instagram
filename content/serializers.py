from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, Story

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    view_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'user', 'caption', 'view_count', 'like_count', 'comment_count', 'created', 'modified')


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Story
        fields = ('id', 'user', 'content', 'caption', 'view_count', 'like_count', 'created', 'modified')
