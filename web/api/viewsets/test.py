from rest_framework import viewsets

from web.api.models import Test
from web.api.serializers import TestSerializer


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer

    def get_queryset(self):
        return Test.objects.filter(device__owner=self.request.user)
