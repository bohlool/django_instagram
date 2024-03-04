from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import ViewLog

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ViewLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ViewLog
        fields = ('id', 'user', 'created', 'modified')
