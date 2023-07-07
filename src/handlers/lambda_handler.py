from aws_lambda_powertools import Logger
from src.services.rekognition_service import (
    detect_labels,
    process_labels,
    detect_text,
    process_text,
)
from src.models.event_model import Event

logger: Logger = Logger()


def lambda_handler(event: Event, context):
    record = event.Records[0]
    bucket_name = record.s3.bucket.name
    object_key = record.s3.object.key

    try:
        detected_labels = detect_labels(bucket_name, object_key)
        process_labels(detected_labels, bucket_name, object_key)

        detected_text = detect_text(bucket_name, object_key)
        process_text(detected_text, bucket_name, object_key)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    return {"statusCode": 200, "body": "Success"}
