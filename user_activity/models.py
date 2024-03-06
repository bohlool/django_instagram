import re

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LikeManager(models.Manager):
    def track_like(self, obj, user):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        super().get_or_create(content_type=content_type, object_id=obj.id, user=user)

    def get_likes_count(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return super().filter(content_type=content_type, object_id=obj.id).count()

    def get_likes(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return super().filter(content_type=content_type, object_id=obj.id)

    def unlike(self, obj, user):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        try:
            like = super().get(content_type=content_type, object_id=obj.id, user=user)
            like.delete()
        except Like.DoesNotExist:
            pass


class Like(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    objects = LikeManager()

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f"{self.content_object} liked by {self.user}"


class CommentManager(models.Manager):
    def create_comment(self, obj, user, text):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        super().create(content_type=content_type, object_id=obj.id, user=user, text=text)

    def get_comments_count(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return super().filter(content_type=content_type, object_id=obj.id).count()

    def get_comments(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        comments = super().filter(content_type=content_type, object_id=obj.id)
        return comments


class Comment(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    mentions = models.ManyToManyField(User, related_name='mentioned_in_comments', blank=True)

    objects = CommentManager()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

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
