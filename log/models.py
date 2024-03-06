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


class ViewManager(models.Manager):
    def track_view(self, obj, user):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        super().create(content_type=content_type, object_id=obj.id, user=user)

    def get_views_count(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return super().filter(content_type=content_type, object_id=obj.id).count()

    def get_views_count_by_user(self, obj, user):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return super().filter(content_type=content_type, object_id=obj.id, user=user).count()

    def get_views(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return super().filter(content_type=content_type, object_id=obj.id)

    def get_views_by_user(self, obj, user):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return super().filter(content_type=content_type, object_id=obj.id, user=user)


class ViewLog(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='view_logs')

    objects = ViewManager()

    def __str__(self):
        return f"{self.content_object} viewed by {self.user}"
