from django.contrib import admin

from notifications.models import TelegramProfile


@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "chat_id")
