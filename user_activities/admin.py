from django.contrib import admin

from .models import Like, Comment


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'user', 'created', 'modified')
    list_filter = ('user',)
    search_fields = ('user__username',)
    readonly_fields = ('created', 'modified')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'user', 'text', 'created', 'modified')
    list_filter = ('user',)
    search_fields = ('text', 'user__username')
    readonly_fields = ('created', 'modified')
