from django.contrib import admin

from view_log.models import ViewLog


@admin.register(ViewLog)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'user', 'created', 'modified')
    list_filter = ('user',)
    search_fields = ('user__username',)
    readonly_fields = ('created', 'modified')
