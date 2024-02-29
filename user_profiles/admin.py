from django.contrib import admin

from .models import Profile, Follow


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'view_count')
    search_fields = ('user__username', 'bio')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'followed')
    search_fields = ('follower__username', 'followed__username')
