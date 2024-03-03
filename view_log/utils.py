from django.contrib.contenttypes.models import ContentType

from .models import View


def track_view(obj, user):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    View.objects.create(content_type=content_type, object_id=obj.id, content_object=obj, user=user)


def get_total_views(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return View.objects.filter(content_type=content_type, object_id=obj.id).count()


def get_views_by_user(obj, user):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return View.objects.filter(content_type=content_type, object_id=obj.id, user=user).count()


def get_viewers(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    views = View.objects.filter(content_type=content_type, object_id=obj.id).values_list('user', flat=True).distinct()
    return views
