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
    follower = UserSerializer(read_only=True)
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Follow
        fields = ('id', 'follower', 'followed', 'is_active', 'created', 'modified')

    def create(self, validated_data):
        follower = validated_data.get("follower")
        followed = validated_data.get('followed')
        is_active = True if followed.profile.is_public else False
        return self.Meta.model.objects.get_or_create(follower=follower, followed=followed,
                                                     defaults={'is_active': is_active})


class FollowResponseSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    followed = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ('id', 'follower', 'followed', 'is_active', 'created', 'modified')
