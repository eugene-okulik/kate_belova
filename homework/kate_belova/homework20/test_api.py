# запускать из директории \kate_belova\homework\kate_belova\homework20
import pytest
import requests

from .functions import (
    get_all_objects,
    create_new_object,
    delete_object,
    get_one_object,
    update_object,
    partially_update_object,
)
from .test_data import (
    data,
    data_empty_name,
    data_special_chars,
    update_data,
    patch_data,
    base_url,
)


@pytest.mark.critical
def test_get_all_objects():
    get_all_objects()


@pytest.mark.parametrize(
    'create_data', [data, data_empty_name, data_special_chars]
)
def test_create_object(create_data):
    created = create_new_object(create_data)
    obj_id = created['id']
    assert obj_id is not None
    assert created['name'] == create_data['name']
    delete_object(obj_id)


def test_get_one_object(new_object):
    obj = get_one_object(new_object)
    assert obj['id'] == new_object
    assert obj['name'] == data['name']


@pytest.mark.medium
def test_update_object(new_object):
    updated = update_object(new_object, update_data)
    assert updated['id'] == str(new_object)
    assert updated['name'] == update_data['name']


def test_partially_update_object(new_object):
    updated = partially_update_object(new_object, patch_data)
    assert updated['id'] == new_object
    assert updated['name'] == patch_data['name']


def test_delete_object():
    created = create_new_object(data)
    obj_id = created['id']
    delete_object(obj_id)
    get_response = requests.get(base_url + f'/object/{obj_id}')
    assert get_response.status_code == 404
