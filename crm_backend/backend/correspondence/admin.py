from django.contrib import admin
from .models import Correspondence

@admin.register(Correspondence)
class CorrespondenceAdmin(admin.ModelAdmin):
	list_display = ("id", "contact", "type", "subject", "timestamp", "created_by", "created_at")
	list_filter = ("type", "contact", "created_by", "timestamp")
	search_fields = ("subject", "body")
	readonly_fields = ("created_at",)