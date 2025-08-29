from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Correspondence
from .serializers import CorrespondenceSerializer

# Create your views here.

class CorrespondenceViewSet(viewsets.ModelViewSet):
	queryset = Correspondence.objects.all().order_by("-created_at")
	serializer_class = CorrespondenceSerializer
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ["contact", "type", "timestamp", "created_by"]
	search_fields = ["subject", "body"]
	ordering_fields = ["timestamp", "created_at"]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
