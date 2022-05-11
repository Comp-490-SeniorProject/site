from rest_framework import status, viewsets
from rest_framework.response import Response

from web.api import aws
from web.api.models import Device
from web.api.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    filterset_fields = ["name"]

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Have to save it to know what its ID is.
        device = self.perform_create(serializer)
        aws_data = {"aws": {}}

        try:
            aws_data["aws"] = aws.create_iot_thing(device.owner_id, device.id)
        except Exception as e:
            # Broad except clause since the Device instance is useless if AWS fails for any reason.
            device.delete()

            if isinstance(e, aws.iot_client.ThrottlingException):
                return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)
            else:
                raise

        # Can't use union yet: see https://github.com/encode/django-rest-framework/pull/8302
        data = {**serializer.data, **aws_data}
        headers = self.get_success_headers(serializer.data)

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        device = self.get_object()
        self.perform_destroy(device)

        aws.delete_iot_thing(device.owner_id, device.id)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        return serializer.save()
