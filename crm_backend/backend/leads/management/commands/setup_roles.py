from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
	help = "Create default roles: manager, agent"

	def handle(self, *args, **options):
		roles = ["manager", "agent"]
		for role in roles:
			group, created = Group.objects.get_or_create(name=role)
			if created:
				self.stdout.write(
					self.style.SUCCESS(f"Created group: {role}")
				)
			else:
				self.stdout.write(
					self.style.WARNING(f"Group {role} already exists")
				)
