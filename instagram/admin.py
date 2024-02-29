from django.contrib import admin

from .models import Post, Media, Like, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'caption', 'view_count')
    list_filter = ('author',)
    search_fields = ('caption',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'media_type')
    list_filter = ('media_type',)
    search_fields = ('post__caption',)


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
