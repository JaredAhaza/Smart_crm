from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Lead(models.Model):
	STATUS_CHOICES = [
		("new", "New"),
		("contacted", "Contacted"),
		("qualified", "Qualified"),
		("lost", "Lost"),
	]
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="leads")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
