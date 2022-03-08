from rest_framework import viewsets

from web.api.models import Parameter
from web.api.serializers import ParameterSerializer


class ParameterViewSet(viewsets.ModelViewSet):
    serializer_class = ParameterSerializer
    filterset_fields = ["test__id", "test__device__id", "name", "unit", "is_manual"]

    def get_queryset(self):
        return Parameter.objects.filter(test__device__owner=self.request.user)
