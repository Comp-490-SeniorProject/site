from rest_framework import viewsets

from web.api.models import NotificationSettings
from web.api.serializers import NotificationSettingsSerializer


class NotificationSettingsViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSettingsSerializer

    def get_queryset(self):
        return NotificationSettings.objects.filter(test__device__owner=self.request.user)
