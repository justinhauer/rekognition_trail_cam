from typing import List, Dict, Any
from aws_lambda_powertools.utilities.parser import BaseModel


class Event(BaseModel):
    Records: List[Dict[str, Any]]
