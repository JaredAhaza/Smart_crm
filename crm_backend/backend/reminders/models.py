from django.db import models
from django.contrib.auth import get_user_model
from leads.models import Lead

User = get_user_model()

class Reminder(models.Model):
	lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="reminders")
	description = models.CharField(max_length=255)
	remind_at = models.DateTimeField()
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reminders")
	is_sent = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.description} - {self.lead.name}"
