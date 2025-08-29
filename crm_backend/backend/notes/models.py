from django.db import models
from django.contrib.auth import get_user_model
from leads.models import Lead

User = get_user_model()

class Note(models.Model):
	lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="notes")
	content = models.TextField()
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="notes")
	created_at = models.DateTimeField(auto_now_add=True)
