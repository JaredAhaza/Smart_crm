from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class AuditLog(models.Model):
	action = models.CharField(max_length=20)  # created/updated/deleted
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.CharField(max_length=64)
	changes = models.JSONField(default=dict)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.action} {self.content_type.model} {self.object_id} by {self.user}"
