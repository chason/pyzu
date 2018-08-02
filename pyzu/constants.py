from typing import Union
from datetime import datetime

import rdflib


OG_NAMESPACES = (
    rdflib.Namespace("http://opengraphprotocol.org/schema/"),
    rdflib.Namespace("http://ogp.me/ns#"),
)

REQUIRED_ATTRIBUTES = ["title", "type", "image", "url", "description"]

OG_TYPES = Union[str, int, float, bool, datetime, list]
