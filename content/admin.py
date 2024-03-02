from django.contrib import admin

from .models import Post, Media


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'caption', 'view_count')
    list_filter = ('user',)
    search_fields = ('caption',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'media_type')
    list_filter = ('media_type',)
    search_fields = ('post__caption',)
