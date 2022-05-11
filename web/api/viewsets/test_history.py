from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from web.api.models import TestHistory
from web.api.serializers import TestHistorySerializer


class TestHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = TestHistorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "test__id",
        "test__parameter__id",
        "test__parameter__device__id",
        "started_at",
        "ended_at",
        "status",
    ]
    ordering_fields = ["started_at", "ended_at"]
    ordering = ["ended_at"]

    def get_queryset(self):
        return TestHistory.objects.filter(test__parameter__device__owner=self.request.user)
