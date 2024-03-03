from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from user_activities.models import Like, Comment
from view_log.models import View
from .models import Post, Media


class LikeInline(GenericTabularInline):
    model = Like
    extra = 1

    fields = ('user',)
    readonly_fields = ('created', 'modified')


class ViewInline(GenericTabularInline):
    model = View
    extra = 1

    fields = ('user',)
    readonly_fields = ('created', 'modified')


class CommentInline(GenericTabularInline):
    model = Comment
    extra = 1

    fields = ('user', 'text')
    readonly_fields = ('created', 'modified')


class MediaInline(admin.TabularInline):
    model = Media
    extra = 3

    fields = ('media_type', 'media')
    readonly_fields = ('created', 'modified')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [MediaInline, ViewInline, LikeInline, CommentInline]
    list_display = ('id', 'user', 'caption', 'view_count')
    list_filter = ('user',)
    search_fields = ('caption',)
    readonly_fields = ('created', 'modified')
    filter_horizontal = ('mentions',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'media_type', 'media')
    list_filter = ('media_type',)
    search_fields = ('post__caption',)
    readonly_fields = ('created', 'modified')
