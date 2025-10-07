from pydantic import BaseModel, Field, model_validator


class DataSchema(BaseModel):
    color: str = Field(description='Цвет объекта')
    size: str = Field(description='Размер объекта')


class RequestObjectSchema(BaseModel):
    data: DataSchema | None = Field(default=None, description='Данные объекта')
    name: str | None = Field(default=None, description='Название объекта')

    @model_validator(mode='after')
    def check_data_or_name(cls, values):
        data = values.data
        name = values.name

        if data is None and name is None:
            raise ValueError('Either "name" or "data" must be provided')
        return values


class ResponseObjectSchema(BaseModel):
    data: DataSchema
    id: int = Field(description='Уникальный идентификатор объекта')
    name: str = Field(description='Название объекта')


class ResponseObjectsSchema(BaseModel):
    data: list[ResponseObjectSchema] = Field(
        description='Список объектов ResponseObjectSchema'
    )
