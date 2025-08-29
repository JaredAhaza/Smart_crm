from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
	list_display = ("id", "lead", "description", "remind_at", "is_sent", "created_by", "created_at")
	list_filter = ("lead", "is_sent", "created_by", "remind_at")
	search_fields = ("description",)
	readonly_fields = ("is_sent", "created_at")