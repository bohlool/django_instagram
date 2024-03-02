from django.contrib.contenttypes.models import ContentType

from .models import Like


def track_like(object, user):
    content_type = ContentType.objects.get_for_model(object.__class__)
    Like.objects.get_or_create(content_type=content_type, object_id=object.id, content_object=object, user=user)


def get_total_likes(object):
    content_type = ContentType.objects.get_for_model(object.__class__)
    return Like.objects.filter(content_type=content_type, object_id=object.id).count()


def get_enthusiasts(object):
    content_type = ContentType.objects.get_for_model(object.__class__)
    fans = Like.objects.filter(content_type=content_type, object_id=object.id).values_list('user', flat=True)
    return fans
