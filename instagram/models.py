import re

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption


class Media(TimeStampedModel):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    image = models.FileField(upload_to='instagram/post/image/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])])
    video = models.FileField(upload_to='instagram/post/video/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    def __str__(self):
        return f"{self.media_type} of {self.post} at {self.created}"


class Like(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post} liked by {self.user}"


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
