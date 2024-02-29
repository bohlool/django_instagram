from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Follow, Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    view_count = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'picture', 'is_public', 'view_count', 'created', 'modified']


class FollowRequestSerializer(serializers.ModelSerializer):
    follower = ProfileSerializer(read_only=True)
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Follow
        fields = ('id', 'follower', 'followed', 'is_active', 'created', 'modified')

    def create(self, validated_data):
        followed = validated_data.get('followed')
        is_active = True if followed.is_public else False
        return self.Meta.model.objects.create(is_active=is_active, **validated_data)


class FollowResponseSerializer(serializers.ModelSerializer):
    follower = ProfileSerializer(read_only=True)
    followed = ProfileSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ('id', 'follower', 'followed', 'is_active', 'created', 'modified')
