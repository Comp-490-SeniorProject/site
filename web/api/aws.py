import logging

import boto3
import orjson

from web.api.models import Parameter, TestHistory, TestStatus

__all__ = ("create_iot_thing", "publish_test")

TOPIC_NAME = "ap/{user_id}/{device_id}"
THING_GROUP_NAME = "ap_thing_group_{user_id}"
THING_NAME = "ap_thing_{user_id}"
POLICY_NAME = f"{THING_GROUP_NAME}_policy"

log = logging.getLogger(__name__)
iot_client = boto3.client("iot")
iot_data_client = boto3.client("iot-data")


def create_iot_thing(user_id: int, device_id: int):
    """Create a new IoT Thing for the given user and device.

    Each user has a separate IoT Thing group for their devices.
    """
    try:
        # Try to get the user's IoT group.
        group_name = THING_GROUP_NAME.format(user_id=user_id)
        thing_group = iot_client.describe_thing_group(thingGroupName=group_name)
    except iot_client.exceptions.ResourceNotFoundException:
        # Create a new group if one cannot be found.
        thing_group = _create_iot_thing_group(user_id)

    # The attributes will be available as variables in the policy.
    attributes = {"attributes": {"device_id": device_id}}
    thing = iot_client.create_thing(
        thingName=THING_NAME.format(user_id=user_id, device_id=device_id),
        attributePayload=orjson.dumps(attributes),
    )

    iot_client.add_thing_to_thing_group(
        thingGroupName=thing_group["thingGroupName"],
        thingGroupArn=thing_group["thingGroupArn"],
        thingName=thing["thingName"],
        thingArn=thing["thingArn"],
    )

    keys_and_cert = iot_client.create_keys_and_certificate(setAsActive=True)
    iot_client.attach_thing_principal(
        thingName=thing["thingName"],
        principal=keys_and_cert["certificateArn"],
    )


def publish_test(parameter_id: int):
    """Publish a new test for the given parameter."""
    parameter = Parameter.objects.get(pk=parameter_id)
    test_history = TestHistory.objects.create(test=parameter.test)
    payload = orjson.dumps(dict(test_history_id=test_history.id, sensor_id=parameter.sensor_id))
    topic = TOPIC_NAME.format(user_id=parameter.device_id, device_id=parameter.sensor_id)

    try:
        # TODO: publish to the topic specific to the device ID.
        response = iot_data_client.publish(topic=topic, payload=payload)
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


def _create_iot_thing_group(user_id: int) -> dict:
    """Return a new IoT Thing group for the given user.

    Attach a new policy to the group which allows the device to connect to the new Thing,
    subscribe to a topic, and receive messages on that topic. The policy only allows a device to
    use its own topic.
    """
    # Both an attribute and a tag may be redundant, but whatever; doesn't seem to hurt.
    group_attributes = {"attributes": {"user_id": user_id}}
    thing_group = iot_client.create_thing_group(
        thingGroupName=THING_GROUP_NAME.format(user_id=user_id),
        thingGroupDescription=f"Group for all devices of user {user_id}.",
        attributes=orjson.dumps(group_attributes),
        tags=[{"user_id": user_id}],
    )

    # The account ID could be retrieved with STS's get_caller_identity().
    # However, parsing an existing ARN avoids an extra API call.
    arn_prefix = ":".join(thing_group["thingGroupArn"].split(":")[:5])

    topic = TOPIC_NAME.format(user_id=user_id, device_id="${iot:Thing.Attributes[device_id]}")
    policy_doc = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": ["iot:Connect"],
                "Resource": [f"{arn_prefix}:client/${{iot:Connection.Thing.ThingName}}"],
            },
            {
                "Effect": "Allow",
                "Action": ["iot:Subscribe"],
                "Resource": [f"{arn_prefix}:topicfilter/{topic}"],
            },
            {
                "Effect": "Allow",
                "Action": ["iot:Receive"],
                "Resource": [f"{arn_prefix}:topic/{topic}"],
            },
        ],
    }

    policy = iot_client.create_policy(
        policyName=POLICY_NAME.format(user_id=user_id),
        policyDocument=orjson.dumps(policy_doc),
        tags=[{"user_id": user_id}],
    )

    # Attach the policy to the group rather than to the certificate.
    iot_client.attach_policy(
        policyName=policy["policyName"],
        target=thing_group["thingGroupArn"],
    )

    return thing_group
