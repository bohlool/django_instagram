from django.contrib.contenttypes.models import ContentType

from .models import Like, Comment


def track_like(obj, user):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    Like.objects.get_or_create(content_type=content_type, object_id=obj.id, content_object=obj, user=user)


def get_likes_count(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return Like.objects.filter(content_type=content_type, object_id=obj.id).count()


def get_likes(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    likes = Like.objects.filter(content_type=content_type, object_id=obj.id).values_list('user', flat=True)
    return likes


def create_comment(obj, user, text):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    Comment.objects.create(content_type=content_type, object_id=obj.id, content_object=obj, user=user, text=text)


def get_comments_count(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return Comment.objects.filter(content_type=content_type, object_id=obj.id).count()


def get_comments(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.id)
    return comments
