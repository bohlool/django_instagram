from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from .models import Story


@shared_task
def remove_old_stories():
    time_threshold = timezone.now() - timedelta(days=1)
    old_stories = Story.objects.filter(created__lt=time_threshold)
    old_stories.update(is_active=False)
