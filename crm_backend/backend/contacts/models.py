from django.db import models
from django.contrib.auth import get_user_model
from leads.models import Lead

User = get_user_model()

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=50, blank=True)
	lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="contacts")
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="contacts")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
