from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Message

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = (
            'id', 'sender', 'receiver', 'message_type', 'text_content', 'audio_file', 'video_file', 'created',
            'modified')
