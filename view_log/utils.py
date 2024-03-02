from django.contrib.contenttypes.models import ContentType

from .models import View


def track_view(object, user):
    content_type = ContentType.objects.get_for_model(object.__class__)
    View.objects.create(content_type=content_type, object_id=object.id, content_object=object, user=user)


def get_total_views(object):
    content_type = ContentType.objects.get_for_model(object.__class__)
    return View.objects.filter(content_type=content_type, object_id=object.id).count()


def get_views_by_user(object, user):
    content_type = ContentType.objects.get_for_model(object.__class__)
    return View.objects.filter(content_type=content_type, object_id=object.id, user=user).count()


def get_viewers(object):
    content_type = ContentType.objects.get_for_model(object.__class__)
    views = View.objects.filter(content_type=content_type, object_id=object.id).values_list('user', flat=True).distinct()
    return views
