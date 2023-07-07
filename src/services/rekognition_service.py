import boto3


def detect_labels(bucket_name, object_key):
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_labels(
        Image={"S3Object": {"Bucket": bucket_name, "Name": object_key}},
        MaxLabels=10,
        MinConfidence=75.0,
    )
    return [label["Name"] for label in response["Labels"]]


def process_labels(labels, bucket_name, object_key):
    label_actions = {
        "Deer": f"Deer detected in the image: s3://{bucket_name}/{object_key}",
        "Human": f"Human detected in the image: s3://{bucket_name}/{object_key}",
        "Animal": f"Animal detected in the image: s3://{bucket_name}/{object_key}",
        "Raccoon": f"Raccoon detected in the image: s3://{bucket_name}/{object_key}",
        "Rabbit": f"Rabbit detected in the image: s3://{bucket_name}/{object_key}",
        "Squirrel": f"Squirrel detected in the image: s3://{bucket_name}/{object_key}",
    }

    for label in labels:
        if label in label_actions:
            logger.info(label_actions[label])
            increment_cloudwatch_metric(label)


def detect_text(bucket_name, object_key):
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_text(
        Image={"S3Object": {"Bucket": bucket_name, "Name": object_key}}
    )
    return [text["DetectedText"] for text in response["TextDetections"]]


def process_text(texts, bucket_name, object_key):
    text_actions = {
        "time": f"Time detected in the image: s3://{bucket_name}/{object_key}",
        "date": f"Date detected in the image: s3://{bucket_name}/{object_key}",
        "temperature": f"Temperature detected in the image: s3://{bucket_name}/{object_key}",
    }

    for text in texts:
        for keyword, action in text_actions.items():
            if keyword in text.lower():
                logger.info(action)
                increment_cloudwatch_metric(keyword)
