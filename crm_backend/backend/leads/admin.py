from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "status", "owner", "created_at", "updated_at")
	list_filter = ("status", "owner", "created_at")
	search_fields = ("name",)
	readonly_fields = ("created_at", "updated_at")