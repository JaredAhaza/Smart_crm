from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ("id", "lead", "content", "created_by", "created_at")
	list_filter = ("lead", "created_by", "created_at")
	search_fields = ("content",)
	readonly_fields = ("created_at",)
