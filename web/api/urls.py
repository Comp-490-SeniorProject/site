from django.urls import include, path
from rest_framework import routers

from .viewsets import (
    DeviceViewSet,
    NotificationSettingsViewSet,
    ParameterViewSet,
    TestHistoryViewSet,
    TestViewSet,
)

router = routers.DefaultRouter()
router.register("devices", DeviceViewSet, basename="device")
router.register(
    "notification_settings", NotificationSettingsViewSet, basename="notification_settings"
)
router.register("parameters", ParameterViewSet, basename="parameter")
router.register("tests", TestViewSet, basename="test")
router.register("test_history", TestHistoryViewSet, basename="test_history")

urlpatterns = [
    path("", include(router.urls)),
]
