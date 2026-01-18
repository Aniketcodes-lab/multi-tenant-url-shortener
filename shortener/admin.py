from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ("short_code", "tenant", "original_url", "clicks", "created_at")
    search_fields = ("short_code", "original_url")
