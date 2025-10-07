__all__ = [
    'BaseAPI',
    'GetObjects',
    'GetObject',
    'CreateObject',
    'UpdateObject',
    'PartiallyUpdateObject',
    'DeleteObject',
]

from test_api_belova.endpoints.base_api import BaseAPI
from test_api_belova.endpoints.create_object import CreateObject
from test_api_belova.endpoints.delete_object import DeleteObject
from test_api_belova.endpoints.get_object import GetObjects, GetObject
from test_api_belova.endpoints.update_object import (
    UpdateObject,
    PartiallyUpdateObject,
)
