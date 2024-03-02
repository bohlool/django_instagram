from django.contrib import admin

from view_log.models import View


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'user')
    list_filter = ('user',)
    search_fields = ('user__username',)
