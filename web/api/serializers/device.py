from rest_framework import serializers

from web.api.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Device
        fields = "__all__"
