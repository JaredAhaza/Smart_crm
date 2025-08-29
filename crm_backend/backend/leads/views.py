from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Lead
from .serializers import LeadSerializer
from .permissions import IsManagerOrNoDelete

# Create your views here.

class LeadViewSet(viewsets.ModelViewSet):
	queryset = Lead.objects.all().order_by("-created_at")
	serializer_class = LeadSerializer
	permission_classes = [IsManagerOrNoDelete]
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ["status", "owner", "created_at"]
	search_fields = ["name", "status"]
	ordering_fields = ["created_at", "updated_at", "name"]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
