from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsManagerOrNoDelete

# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all().order_by("-created_at")
	serializer_class = ContactSerializer
	permission_classes = [IsManagerOrNoDelete]
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ["lead", "owner", "created_at"]
	search_fields = ["first_name", "last_name", "email", "phone"]
	ordering_fields = ["created_at", "updated_at", "last_name"]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
