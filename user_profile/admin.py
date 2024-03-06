from django.contrib import admin

from .models import Profile, Follow


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'view_count', 'created', 'modified')
    search_fields = ('user__username', 'bio')
    readonly_fields = ('created', 'modified',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'followed', 'created', 'modified')
    search_fields = ('follower__username', 'followed__username')
    list_filter = ('follower', 'followed')
    readonly_fields = ('created', 'modified',)
