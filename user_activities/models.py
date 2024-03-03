import re

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from content.models import Post

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Like(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content_object} liked by {self.user}"


class Comment(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    mentions = models.ManyToManyField(User, related_name='mentioned_in_comments', blank=True)

    def __str__(self):
        return f"{self.text} commented by {self.user}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.mentions.clear()  # Clear existing mentions to avoid duplicates
        mentioned_usernames = re.findall(r'@(\w+)', self.text)
        for username in mentioned_usernames:
            try:
                user = User.objects.get(username=username)
                self.mentions.add(user)
            except User.DoesNotExist:
                pass
