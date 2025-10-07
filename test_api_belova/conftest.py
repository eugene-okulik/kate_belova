import pytest

from test_api_belova.endpoints import (
    CreateObject,
    DeleteObject,
    GetObjects,
    GetObject,
)
from test_api_belova.schemas import RequestObjectSchema
from test_api_belova.test_data import create_data


@pytest.fixture(scope='session', autouse=True)
def before_all_after_all():
    print('\nStart testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def before_and_after_each():
    print('\nbefore test')
    yield
    print('after test')


@pytest.fixture
def get_objects_api():
    return GetObjects()


@pytest.fixture
def get_object_api():
    return GetObject()


@pytest.fixture
def created_object():
    create_api = CreateObject()
    test_data = RequestObjectSchema(**create_data[0]).model_dump()
    create_api.create_object(test_data)
    obj_id = create_api.id

    yield test_data, obj_id

    delete_api = DeleteObject(obj_id)
    delete_api.delete_object()


@pytest.fixture
def object_id(created_object):
    return created_object[1]
