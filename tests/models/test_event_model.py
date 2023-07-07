from src.models.event_model import Event
from aws_lambda_powertools.utilities.parser import from_dict


def test_event_model():
    event_data = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": "my-bucket"},
                    "object": {"key": "my-object.jpg"},
                }
            }
        ]
    }

    event = from_dict(data=event_data, model=Event)

    assert isinstance(event, Event)
    assert isinstance(event.Records, list)
    assert len(event.Records) == 1
    assert isinstance(event.Records[0], dict)
    assert event.Records[0]["s3"]["bucket"]["name"] == "my-bucket"
    assert event.Records[0]["s3"]["object"]["key"] == "my-object.jpg"
