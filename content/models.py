import re

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

from view_log.utils import get_total_views

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True, null=True)
    mentions = models.ManyToManyField(User, related_name='mentioned_in_posts', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.caption

    @property
    def view_count(self):
        return get_total_views(self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.mentions.clear()  # Clear existing mentions to avoid duplicates
        mentioned_usernames = re.findall(r'@(\w+)', self.caption)
        for username in mentioned_usernames:
            try:
                user = User.objects.get(username=username)
                self.mentions.add(user)
            except User.DoesNotExist:
                pass


class Media(TimeStampedModel):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    image = models.FileField(upload_to='content/post/image/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])])
    video = models.FileField(upload_to='content/post/video/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    def __str__(self):
        return f"{self.media_type} of {self.post} at {self.created}"


class Story(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.FileField(upload_to='content/stories/')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Story number {self.pk} of {self.user}"
