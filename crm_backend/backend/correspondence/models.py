from django.db import models
from django.contrib.auth import get_user_model
from contacts.models import Contact

User = get_user_model()

class Correspondence(models.Model):
	TYPE_CHOICES = [("email","Email"),("call","Call"),("meeting","Meeting")]
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="correspondences")
	type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	subject = models.CharField(max_length=255, blank=True)
	body = models.TextField(blank=True)
	timestamp = models.DateTimeField()
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="correspondences")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.type} - {self.contact.first_name} {self.contact.last_name}"
