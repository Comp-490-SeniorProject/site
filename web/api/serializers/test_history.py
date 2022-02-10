from rest_framework import serializers

from web.api.models import TestHistory


class TestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestHistory
        fields = "__all__"
