import pytest

from .functions import (
    create_new_object,
    delete_object,
)
from .test_data import data


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
def new_object():
    """Создание объекта перед тестом и удаление после"""
    created = create_new_object(data)
    obj_id = created['id']
    yield created
    delete_object(obj_id)
