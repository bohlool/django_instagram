from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from log.models import ViewLog

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.FileField(upload_to='user_profile/profile/pictures/', null=True, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @property
    def view_count(self):
        return ViewLog.objects.get_views_count(self)

    def get_views(self):
        return ViewLog.objects.get_views_count(self)

    @property
    def post_count(self):
        return ViewLog.objects.get_views_count(self)

    def get_posts(self):
        return self.user.posts

    @property
    def stories_count(self):
        return self.user.stories.filter(is_active=True).count()

    def get_stories(self):
        return self.user.stories.filter(is_active=True)

    @property
    def following_count(self):
        return Follow.objects.get_following_count(self.user)

    def get_following(self):
        return Follow.objects.get_following(self.user)

    @property
    def followers_count(self):
        return Follow.objects.get_followers_count(self.user)

    def get_followers(self):
        return Follow.objects.get_followers(self.user)

    @property
    def follow_requests_count(self):
        return Follow.objects.get_follow_requests_count(self.user)

    def get_follow_requests(self):
        return Follow.objects.get_follow_requests(self.user)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class FollowManager(models.Manager):
    def get_following_count(self, user):
        return super().filter(follower=user, is_active=True).count()

    def get_following(self, user):
        return super().filter(follower=user, is_active=True)

    def get_followers_count(self, user):
        return super().filter(followed=user, is_active=True).count()

    def get_followers(self, user):
        return super().filter(followed=user, is_active=True).count()

    def get_follow_requests_count(self, user):
        return super().filter(followed=user, is_active=False).count()

    def get_follow_requests(self, user):
        return super().filter(followed=user, is_active=False).count()


class Follow(TimeStampedModel):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    objects = FollowManager()

    def __str__(self):
        return f'{self.follower} follows {self.followed}'
