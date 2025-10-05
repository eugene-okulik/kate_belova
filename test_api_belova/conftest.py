import pytest

from test_api_belova.endpoints import CreateObject, DeleteObject
from test_api_belova.models import RequestObjectModel
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
def object_data():
    create_object_api = CreateObject()
    create_object_data = RequestObjectModel(**create_data[0]).model_dump()
    create_object_api.post_response(create_object_data)

    create_object_api.assert_response_is_200()
    create_object_api.assert_object_name(create_object_data)
    create_object_api.assert_object_data(create_object_data)

    id = create_object_api.id
    yield create_object_data, id

    id = create_object_api.id
    delete_object_api = DeleteObject(id)
    delete_object_api.delete_response()
    delete_object_api.assert_response_is_200()
    delete_object_api.assert_delete_message()
