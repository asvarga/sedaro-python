# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sedaro import schemas  # noqa: F401


class BranchScenarioTemplateRes(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "shareable",
            "dataSchema",
            "simulationRequired",
            "data",
            "sharePwRqd",
            "dateModified",
            "repository",
            "uuid",
            "dateCreated",
            "name",
            "numSimulations",
            "id",
            "user",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            id = schemas.IntSchema
            dateCreated = schemas.DateTimeSchema
            dateModified = schemas.DateTimeSchema
            simulationRequired = schemas.BoolSchema
            repository = schemas.IntSchema
            user = schemas.IntSchema
            uuid = schemas.UUIDSchema
            shareable = schemas.BoolSchema
            sharePwRqd = schemas.BoolSchema
            numSimulations = schemas.IntSchema
            dataSchema = schemas.DictSchema
        
            @staticmethod
            def data() -> typing.Type['ScenarioTemplate']:
                return ScenarioTemplate
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 300
            __annotations__ = {
                "name": name,
                "id": id,
                "dateCreated": dateCreated,
                "dateModified": dateModified,
                "simulationRequired": simulationRequired,
                "repository": repository,
                "user": user,
                "uuid": uuid,
                "shareable": shareable,
                "sharePwRqd": sharePwRqd,
                "numSimulations": numSimulations,
                "dataSchema": dataSchema,
                "data": data,
                "description": description,
            }
    
    shareable: MetaOapg.properties.shareable
    dataSchema: MetaOapg.properties.dataSchema
    simulationRequired: MetaOapg.properties.simulationRequired
    data: 'ScenarioTemplate'
    sharePwRqd: MetaOapg.properties.sharePwRqd
    dateModified: MetaOapg.properties.dateModified
    repository: MetaOapg.properties.repository
    uuid: MetaOapg.properties.uuid
    dateCreated: MetaOapg.properties.dateCreated
    name: MetaOapg.properties.name
    numSimulations: MetaOapg.properties.numSimulations
    id: MetaOapg.properties.id
    user: MetaOapg.properties.user
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateModified"]) -> MetaOapg.properties.dateModified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["simulationRequired"]) -> MetaOapg.properties.simulationRequired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repository"]) -> MetaOapg.properties.repository: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareable"]) -> MetaOapg.properties.shareable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sharePwRqd"]) -> MetaOapg.properties.sharePwRqd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numSimulations"]) -> MetaOapg.properties.numSimulations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSchema"]) -> MetaOapg.properties.dataSchema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ScenarioTemplate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "id", "dateCreated", "dateModified", "simulationRequired", "repository", "user", "uuid", "shareable", "sharePwRqd", "numSimulations", "dataSchema", "data", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateModified"]) -> MetaOapg.properties.dateModified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["simulationRequired"]) -> MetaOapg.properties.simulationRequired: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repository"]) -> MetaOapg.properties.repository: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareable"]) -> MetaOapg.properties.shareable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sharePwRqd"]) -> MetaOapg.properties.sharePwRqd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numSimulations"]) -> MetaOapg.properties.numSimulations: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSchema"]) -> MetaOapg.properties.dataSchema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'ScenarioTemplate': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "id", "dateCreated", "dateModified", "simulationRequired", "repository", "user", "uuid", "shareable", "sharePwRqd", "numSimulations", "dataSchema", "data", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        shareable: typing.Union[MetaOapg.properties.shareable, bool, ],
        dataSchema: typing.Union[MetaOapg.properties.dataSchema, dict, frozendict.frozendict, ],
        simulationRequired: typing.Union[MetaOapg.properties.simulationRequired, bool, ],
        data: 'ScenarioTemplate',
        sharePwRqd: typing.Union[MetaOapg.properties.sharePwRqd, bool, ],
        dateModified: typing.Union[MetaOapg.properties.dateModified, str, datetime, ],
        repository: typing.Union[MetaOapg.properties.repository, decimal.Decimal, int, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, ],
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        numSimulations: typing.Union[MetaOapg.properties.numSimulations, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        user: typing.Union[MetaOapg.properties.user, decimal.Decimal, int, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BranchScenarioTemplateRes':
        return super().__new__(
            cls,
            *args,
            shareable=shareable,
            dataSchema=dataSchema,
            simulationRequired=simulationRequired,
            data=data,
            sharePwRqd=sharePwRqd,
            dateModified=dateModified,
            repository=repository,
            uuid=uuid,
            dateCreated=dateCreated,
            name=name,
            numSimulations=numSimulations,
            id=id,
            user=user,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro.model.scenario_template import ScenarioTemplate
