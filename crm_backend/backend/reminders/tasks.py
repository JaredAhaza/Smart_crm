from celery import shared_task
from django.utils import timezone
from .models import Reminder

@shared_task
def process_due_reminders():
	"""Process all due reminders"""
	for reminder in Reminder.objects.filter(is_sent=False, remind_at__lte=timezone.now()):
		# Here you would send email/SMS notification
		# For now, just mark as sent
		reminder.is_sent = True
		reminder.save()
		print(f"Processed reminder: {reminder.description} for {reminder.lead.name}")
	
	return f"Processed {Reminder.objects.filter(is_sent=False, remind_at__lte=timezone.now()).count()} reminders"
