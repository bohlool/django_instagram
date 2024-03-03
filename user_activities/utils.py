from django.contrib.contenttypes.models import ContentType

from .models import Like


def track_like(obj, user):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    Like.objects.get_or_create(content_type=content_type, object_id=obj.id, content_object=obj, user=user)


def get_total_likes(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return Like.objects.filter(content_type=content_type, object_id=obj.id).count()


def get_enthusiasts(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    fans = Like.objects.filter(content_type=content_type, object_id=obj.id).values_list('user', flat=True)
    return fans
