from django_q.models import Schedule
from rest_framework import serializers

from web.api.models import Test


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["schedule_type", "minutes", "next_run"]


class TestSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=False)

    class Meta:
        model = Test
        fields = "__all__"

    def create(self, validated_data):
        schedule = Schedule.objects.create(
            func="print",
            args=f"'Running test {validated_data['name']} for param {validated_data['parameter']}'",
            **validated_data.pop("schedule"),
        )
        return Test.objects.create(**validated_data, schedule=schedule)

    def update(self, instance, validated_data):
        schedule_serializer = self.fields["schedule"]
        schedule_serializer.update(instance.schedule, validated_data.pop("schedule"))
        return super().update(instance, validated_data)
