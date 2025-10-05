import allure
import pytest

from test_api_belova.endpoints import (
    CreateObject,
    DeleteObject,
    GetObjects,
    GetObject,
    UpdateObject,
    PartiallyUpdateObject,
)
from test_api_belova.models import RequestObjectModel
from test_api_belova.test_data import create_data, update_data, patch_data


@pytest.mark.crud
@pytest.mark.regression
class TestObjects:
    @allure.feature('Objects')
    @allure.story('Get objects')
    @allure.title('Получение всех объектов')
    @pytest.mark.smoke
    @pytest.mark.get
    def test_get_all_objects(self):
        get_objects_api = GetObjects()
        get_objects_api.get_response()

        get_objects_api.assert_response_is_200()
        get_objects_api.assert_has_objects()

    @allure.feature('Objects')
    @allure.story('Get object')
    @allure.title('Получение одного объекта по его id')
    @pytest.mark.smoke
    @pytest.mark.get
    def test_get_object(self, object_data):
        data, id = object_data
        get_object_api = GetObject(id)
        get_object_api.get_response()

        get_object_api.assert_response_is_200()
        get_object_api.assert_object_id(id)
        get_object_api.assert_object_name(data)
        get_object_api.assert_object_data(data)

    @allure.feature('Objects')
    @allure.story('Create object')
    @allure.title('Создание нового объекта')
    @pytest.mark.smoke
    @pytest.mark.create
    @pytest.mark.parametrize(
        'test_data',
        create_data,
        ids=[f'Create object: {data["name"]}' for data in create_data],
    )
    def test_create_new_object(self, test_data):
        create_object_api = CreateObject()
        create_object_data = RequestObjectModel(**test_data).model_dump()
        create_object_api.post_response(create_object_data)

        create_object_api.assert_response_is_200()
        create_object_api.assert_object_name(create_object_data)
        create_object_api.assert_object_data(create_object_data)

        id = create_object_api.id
        delete_object_api = DeleteObject(id)
        delete_object_api.delete_response()
        delete_object_api.assert_response_is_200()
        delete_object_api.assert_delete_message()

    @allure.feature('Objects')
    @allure.story('Update object')
    @allure.title('Полная замена (обновление) объекта по его id')
    @pytest.mark.update
    def test_update_object(self, object_data):
        id = object_data[1]
        update_object_api = UpdateObject(id)
        update_object_data = RequestObjectModel(**update_data).model_dump()
        update_object_api.put_response(update_object_data)

        update_object_api.assert_response_is_200()
        update_object_api.assert_object_id(id)
        update_object_api.assert_object_name(update_object_data)
        update_object_api.assert_object_data(update_object_data)

    @allure.feature('Objects')
    @allure.story('Partially update object')
    @allure.title('Частичная замена (одного или нескольких полей) объекта')
    @pytest.mark.partially_update
    def test_partially_update_object(self, object_data):
        data, id = object_data
        update_object_api = PartiallyUpdateObject(id)
        update_object_data = RequestObjectModel(**patch_data).model_dump(
            exclude_none=True
        )
        update_object_api.patch_response(update_object_data)
        data.update(update_object_data)

        update_object_api.assert_response_is_200()
        update_object_api.assert_object_id(id)
        update_object_api.assert_object_name(data)
        update_object_api.assert_object_data(data)

    @allure.feature('Objects')
    @allure.story('Delete object')
    @allure.title('Удаление объекта')
    @pytest.mark.smoke
    @pytest.mark.delete
    def test_delete_object(self):
        create_object_api = CreateObject()
        create_object_data = RequestObjectModel(**create_data[0]).model_dump()
        create_object_api.post_response(create_object_data)

        id = create_object_api.id
        delete_object_api = DeleteObject(id)
        delete_object_api.delete_response()
        delete_object_api.assert_response_is_200()
        delete_object_api.assert_delete_message()

        get_object_api = GetObject(id)
        get_object_api.get_response()
        get_object_api.assert_response_is_404()
        get_object_api.assert_error_message()
