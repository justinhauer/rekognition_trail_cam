from src.utils.cloudwatch_metrics import increment_cloudwatch_metric
from botocore.stub import Stubber
import boto3


def test_increment_cloudwatch_metric():
    cloudwatch = boto3.client("cloudwatch")
    stubber = Stubber(cloudwatch)
    expected_params = {
        "Namespace": "CustomMetrics",
        "MetricData": [{"MetricName": "label", "Value": 1, "Unit": "Count"}],
    }
    stubber.add_response("put_metric_data", {}, expected_params)

    with stubber:
        increment_cloudwatch_metric("label")

    stubber.assert_no_pending_responses()
