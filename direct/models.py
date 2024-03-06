from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(TimeStampedModel):
    MESSAGE_TYPES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message_type = models.CharField(max_length=5, choices=MESSAGE_TYPES)
    text_content = models.TextField(blank=True, null=True)
    audio_file = models.FileField(upload_to='direct/messages/audio/', blank=True, null=True)
    video_file = models.FileField(upload_to='direct/messages/video/', blank=True, null=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('-created',)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.created}"
