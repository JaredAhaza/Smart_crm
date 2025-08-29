from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ("id", "first_name", "last_name", "email", "phone", "lead", "owner", "created_at")
	list_filter = ("lead", "owner", "created_at")
	search_fields = ("first_name", "last_name", "email", "phone")
	readonly_fields = ("created_at", "updated_at")
