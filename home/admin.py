from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'expires_at')
    list_filter = ('created_at', 'expires_at')
    search_fields = ('title', 'content', 'user__username')