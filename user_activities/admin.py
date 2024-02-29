from django.contrib import admin

from .models import Like, Comment


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user')
    list_filter = ('user',)
    search_fields = ('post__caption', 'user__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text')
    list_filter = ('user',)
    search_fields = ('post__caption', 'user__username')
