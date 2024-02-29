from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'message_type', 'created')
    list_filter = ('message_type',)
    search_fields = ('sender__username', 'receiver__username')
