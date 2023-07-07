from src.handlers.lambda_handler import lambda_handler
from src.models.event_model import Event
from unittest.mock import MagicMock


def test_lambda_handler():
    event = Event(
        Records=[...]
    )  # Figure out what the event looks like and fill this in....

    context = MagicMock()
    response = lambda_handler(event, context)

    assert response["statusCode"] == 200
    assert response["body"] == "Success"
