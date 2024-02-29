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
    image = models.FileField(upload_to='content/post/image/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])])
    video = models.FileField(upload_to='content/post/video/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    def __str__(self):
        return f"{self.media_type} of {self.post} at {self.created}"
