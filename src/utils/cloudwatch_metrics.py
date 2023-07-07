import boto3
from botocore.exceptions import ClientError
from aws_lambda_powertools import Logger

logger: Logger = Logger()
cloudwatch = boto3.client("cloudwatch")


def increment_cloudwatch_metric(label):
    try:
        cloudwatch.put_metric_data(
            Namespace="CustomMetrics",
            MetricData=[{"MetricName": label, "Value": 1, "Unit": "Count"}],
        )
    except ClientError as e:
        logger.error(f"Failed to publish CloudWatch metric: {str(e)}")
