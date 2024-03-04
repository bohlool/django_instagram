from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Follow, Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User.objects.create_user(username, password=password, first_name=first_name, last_name=last_name)
        return user


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


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'password', 'confirm_password')

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')
        if password == confirm_password:
            instance.set_password(password)
            instance.save()
        else:
            raise serializers.ValidationError(
                "The passwords do not match"
            )
        return instance


class ChangeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
