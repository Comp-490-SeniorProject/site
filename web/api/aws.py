import logging

import boto3

from web.api.models import Parameter, TestHistory, TestStatus

__all__ = ("iot_data_client", "publish_test")

log = logging.getLogger(__name__)
iot_data_client = boto3.client("iot-data")


def publish_test(parameter_id: int):
    """Publish a new test for the given parameter."""
    parameter = Parameter.objects.get(pk=parameter_id)
    test_history = TestHistory.objects.create(test=parameter.test)
    payload = f"<{test_history.id}, {parameter.sensor_id}>"

    try:
        # TODO: publish to the topic specific to the device ID.
        response = iot_data_client.publish(topic="test/dc/subtopic", payload=payload)
    except iot_data_client.exceptions.ClientError:
        log.exception(
            "Failed to publish test %d for sensor %d on device %d.",
            test_history.id,
            parameter.sensor_id,
            parameter.device_id,
        )
        test_history.status = TestStatus.FAILED
        test_history.save()
    else:
        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode", "unknown")
        if status == 200:
            log.info(
                "Published test %d for sensor %d on device %d.",
                test_history.id,
                parameter.sensor_id,
                parameter.device_id,
            )
        else:
            log.error(
                "Failed to publish test %d for sensor %d on device %d: status code %d.",
                test_history.id,
                parameter.sensor_id,
                parameter.device_id,
                status,
                extra=dict(response=response),
            )
            test_history.status = TestStatus.FAILED
            test_history.save()
