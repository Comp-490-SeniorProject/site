from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from web.api.models import Test
from web.api.serializers import TestSerializer


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "name",
        "created_at",
        "frequency",
        "parameter__id",
        "parameter__type",
        "parameter__sensor_id",
        "parameter__device__id",
    ]
    ordering_fields = ["created_at"]
    ordering = ["created_at"]

    def get_queryset(self):
        return Test.objects.filter(parameter__device__owner=self.request.user)
