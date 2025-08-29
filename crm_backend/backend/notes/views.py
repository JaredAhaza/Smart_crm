from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = Note.objects.all().order_by("-created_at")
	serializer_class = NoteSerializer
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ["lead", "created_by", "created_at"]
	search_fields = ["content"]
	ordering_fields = ["created_at"]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
