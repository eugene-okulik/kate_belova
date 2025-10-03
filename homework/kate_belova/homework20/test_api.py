# запускать из директории \kate_belova\homework\kate_belova\homework20
import allure
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


@allure.feature('Objects')
@allure.story('Get objects')
@allure.title('Получение всех объектов')
@pytest.mark.critical
def test_get_all_objects():
    get_all_objects()


@allure.feature('Objects')
@allure.story('Create object')
@allure.title('Создание нового объекта')
@pytest.mark.parametrize(
    'create_data', [data, data_empty_name, data_special_chars]
)
def test_create_object(create_data):
    created = create_new_object(create_data)
    with allure.step('Assert object id is not None'):
        obj_id = created['id']
        assert obj_id is not None
    with allure.step('Assert object name matches the one expected'):
        assert created['name'] == create_data['name']
    delete_object(obj_id)


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Получение одного объекта по его id')
def test_get_one_object(new_object):
    obj = get_one_object(new_object)
    with allure.step('Assert object id is not None'):
        assert obj['id'] == new_object
    with allure.step('Assert object name matches the one expected'):
        assert obj['name'] == data['name']


@allure.feature('Objects')
@allure.story('Update object')
@allure.title('Полная замена (обновление) объекта по его id')
@pytest.mark.medium
def test_update_object(new_object):
    updated = update_object(new_object, update_data)
    with allure.step('Assert object id matches the one expected'):
        assert updated['id'] == str(new_object)
    with allure.step('Assert object name matches the one expected'):
        assert updated['name'] == update_data['name']


@allure.feature('Objects')
@allure.story('Partially update object')
@allure.title('Частичная замена (одного или нескольких полей) объекта')
def test_partially_update_object(new_object):
    updated = partially_update_object(new_object, patch_data)
    with allure.step('Assert object id matches the one expected'):
        assert updated['id'] == new_object
    with allure.step('Assert object name matches the one expected'):
        assert updated['name'] == patch_data['name']


@allure.feature('Objects')
@allure.story('Delete object')
@allure.title('Удаление объекта')
def test_delete_object():
    created = create_new_object(data)
    obj_id = created['id']
    delete_object(obj_id)
    with allure.step('An attempt to get deleted object by id'):
        get_response = requests.get(base_url + f'/object/{obj_id}')
    with allure.step('Assert status code is 404'):
        assert get_response.status_code == 404
