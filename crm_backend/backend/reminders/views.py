from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Reminder
from .serializers import ReminderSerializer

# Create your views here.

class ReminderViewSet(viewsets.ModelViewSet):
	queryset = Reminder.objects.all().order_by("-created_at")
	serializer_class = ReminderSerializer
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ["lead", "is_sent", "created_by", "remind_at"]
	search_fields = ["description"]
	ordering_fields = ["remind_at", "created_at"]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
