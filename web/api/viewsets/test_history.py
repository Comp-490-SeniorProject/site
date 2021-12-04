from rest_framework import viewsets

from web.api.models import TestHistory
from web.api.serializers import TestHistorySerializer


class TestHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = TestHistorySerializer

    def get_queryset(self):
        return TestHistory.objects.filter(test__device__owner=self.request.user)
