from rest_framework import serializers
from .models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
	content_type_name = serializers.CharField(source='content_type.model', read_only=True)
	user_name = serializers.CharField(source='user.username', read_only=True)
	
	class Meta:
		model = AuditLog
		fields = "__all__"
		read_only_fields = ("action", "user", "content_type", "object_id", "changes", "created_at")
