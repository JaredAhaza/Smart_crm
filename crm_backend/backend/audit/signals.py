from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.contrib.contenttypes.models import ContentType
from leads.models import Lead
from contacts.models import Contact
from .models import AuditLog

TRACKED_MODELS = (Lead, Contact)

def get_request_user():
	"""Get the current user from the request"""
	import threading
	thread_local = threading.local()
	return getattr(thread_local, 'current_user', None)

def set_request_user(user):
	"""Set the current user for the request"""
	import threading
	thread_local = threading.local()
	thread_local.current_user = user

@receiver(pre_save)
def before_save(sender, instance, **kwargs):
	if sender in TRACKED_MODELS and instance.pk:
		try:
			old = sender.objects.get(pk=instance.pk)
			instance._audit_old = model_to_dict(old)
		except sender.DoesNotExist:
			instance._audit_old = {}

@receiver(post_save)
def after_save(sender, instance, created, **kwargs):
	if sender in TRACKED_MODELS:
		ct = ContentType.objects.get_for_model(sender)
		old = getattr(instance, "_audit_old", {})
		new = model_to_dict(instance)
		
		# Calculate changes
		changes = {}
		for key in new.keys():
			if old.get(key) != new.get(key):
				changes[key] = {"from": old.get(key), "to": new.get(key)}
		
		AuditLog.objects.create(
			action="created" if created else "updated",
			user=get_request_user(),
			content_type=ct,
			object_id=str(instance.pk),
			changes=changes,
		)

@receiver(post_delete)
def after_delete(sender, instance, **kwargs):
	if sender in TRACKED_MODELS:
		ct = ContentType.objects.get_for_model(sender)
		AuditLog.objects.create(
			action="deleted",
			user=get_request_user(),
			content_type=ct,
			object_id=str(instance.pk),
			changes={},
		)
