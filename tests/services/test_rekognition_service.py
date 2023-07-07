from src.services.rekognition_service import (
    detect_labels,
    process_labels,
    detect_text,
    process_text,
)
import boto3
from botocore.stub import Stubber


def test_detect_labels():
    rekognition = boto3.client("rekognition")
    stubber = Stubber(rekognition)

    expected_response = {
        "Labels": [{"Name": "Label1"}, {"Name": "Label2"}, {"Name": "Label3"}]
    }

    stubber.add_response("detect_labels", expected_response)

    with stubber:
        labels = detect_labels("bucket-name", "object-key")

    assert labels == ["Label1", "Label2", "Label3"]


def test_process_labels():
    labels = ["Label1", "Label2", "Label3"]
    bucket_name = "bucket-name"
    object_key = "object-key"

    process_labels(labels, bucket_name, object_key)


def test_detect_text():
    rekognition = boto3.client("rekognition")
    stubber = Stubber(rekognition)

    expected_response = {
        "TextDetections": [
            {"DetectedText": "Time: 10:30 AM"},
            {"DetectedText": "Date: July 10, 2023"},
            {"DetectedText": "Temperature: 70°F"},
        ]
    }

    stubber.add_response("detect_text", expected_response)

    with stubber:
        texts = detect_text("bucket-name", "object-key")

    assert texts == ["Time: 10:30 AM", "Date: July 10, 2023", "Temperature: 70°F"]


def test_process_text():
    texts = ["Time: 10:30 AM", "Date: July 10, 2023", "Temperature: 25°C"]
    bucket_name = "bucket-name"
    object_key = "object-key"

    process_text(texts, bucket_name, object_key)
