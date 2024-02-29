from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Like, Comment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created', 'modified')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    mentions = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'text', 'mentions', 'created', 'modified')
