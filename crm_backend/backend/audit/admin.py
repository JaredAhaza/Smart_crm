from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
	list_display = ("id", "action", "user", "content_type", "object_id", "created_at")
	list_filter = ("action", "content_type", "user", "created_at")
	search_fields = ("object_id",)
	readonly_fields = ("action", "user", "content_type", "object_id", "changes", "created_at")