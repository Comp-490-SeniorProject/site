from rest_framework import viewsets

from web.api.models import Parameter
from web.api.serializers import ParameterSerializer


class ParameterViewSet(viewsets.ModelViewSet):
    serializer_class = ParameterSerializer
    filterset_fields = [
        "name",
        "unit",
        "type",
        "sensor_id",
        "device__id",
        "test__id",
    ]

    def get_queryset(self):
        return Parameter.objects.filter(device__owner=self.request.user)
