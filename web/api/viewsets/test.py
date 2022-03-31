from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from web.api.models import Test
from web.api.serializers import TestSerializer


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "name",
        "parameter__id",
        "parameter__type",
        "parameter__sensor_id",
        "parameter__device__id",
        "schedule__next_run",
        "schedule__schedule_type",
    ]
    ordering_fields = ["schedule__next_run"]
    ordering = ["schedule__next_run"]

    def get_queryset(self):
        return Test.objects.filter(parameter__device__owner=self.request.user)
