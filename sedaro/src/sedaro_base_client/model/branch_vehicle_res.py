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

from sedaro_base_client import schemas  # noqa: F401


class BranchVehicleRes(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "shareable",
            "blockGroupNames",
            "dataSchema",
            "simulationRequired",
            "blockIdToTypeMap",
            "data",
            "sharePwRqd",
            "dateModified",
            "repository",
            "uuid",
            "mission",
            "dateCreated",
            "name",
            "numSimulations",
            "id",
            "user",
            "blockClassToBlockGroupMap",
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
            
            
            class repository(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.DictSchema
                    any_of_1 = schemas.IntSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'repository':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class mission(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.DictSchema
                    any_of_1 = schemas.IntSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'mission':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class user(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.DictSchema
                    any_of_1 = schemas.IntSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'user':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            uuid = schemas.UUIDSchema
            shareable = schemas.BoolSchema
            sharePwRqd = schemas.BoolSchema
            numSimulations = schemas.IntSchema
            dataSchema = schemas.DictSchema
        
            @staticmethod
            def data() -> typing.Type['VehicleTemplate']:
                return VehicleTemplate
            
            
            class blockIdToTypeMap(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'blockIdToTypeMap':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class blockClassToBlockGroupMap(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'blockClassToBlockGroupMap':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class blockGroupNames(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'blockGroupNames':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
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
                "mission": mission,
                "user": user,
                "uuid": uuid,
                "shareable": shareable,
                "sharePwRqd": sharePwRqd,
                "numSimulations": numSimulations,
                "dataSchema": dataSchema,
                "data": data,
                "blockIdToTypeMap": blockIdToTypeMap,
                "blockClassToBlockGroupMap": blockClassToBlockGroupMap,
                "blockGroupNames": blockGroupNames,
                "description": description,
            }
    
    shareable: MetaOapg.properties.shareable
    blockGroupNames: MetaOapg.properties.blockGroupNames
    dataSchema: MetaOapg.properties.dataSchema
    simulationRequired: MetaOapg.properties.simulationRequired
    blockIdToTypeMap: MetaOapg.properties.blockIdToTypeMap
    data: 'VehicleTemplate'
    sharePwRqd: MetaOapg.properties.sharePwRqd
    dateModified: MetaOapg.properties.dateModified
    repository: MetaOapg.properties.repository
    uuid: MetaOapg.properties.uuid
    mission: MetaOapg.properties.mission
    dateCreated: MetaOapg.properties.dateCreated
    name: MetaOapg.properties.name
    numSimulations: MetaOapg.properties.numSimulations
    id: MetaOapg.properties.id
    user: MetaOapg.properties.user
    blockClassToBlockGroupMap: MetaOapg.properties.blockClassToBlockGroupMap
    
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
    def __getitem__(self, name: typing_extensions.Literal["mission"]) -> MetaOapg.properties.mission: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'VehicleTemplate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockIdToTypeMap"]) -> MetaOapg.properties.blockIdToTypeMap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockClassToBlockGroupMap"]) -> MetaOapg.properties.blockClassToBlockGroupMap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockGroupNames"]) -> MetaOapg.properties.blockGroupNames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "id", "dateCreated", "dateModified", "simulationRequired", "repository", "mission", "user", "uuid", "shareable", "sharePwRqd", "numSimulations", "dataSchema", "data", "blockIdToTypeMap", "blockClassToBlockGroupMap", "blockGroupNames", "description", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["mission"]) -> MetaOapg.properties.mission: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'VehicleTemplate': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockIdToTypeMap"]) -> MetaOapg.properties.blockIdToTypeMap: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockClassToBlockGroupMap"]) -> MetaOapg.properties.blockClassToBlockGroupMap: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockGroupNames"]) -> MetaOapg.properties.blockGroupNames: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "id", "dateCreated", "dateModified", "simulationRequired", "repository", "mission", "user", "uuid", "shareable", "sharePwRqd", "numSimulations", "dataSchema", "data", "blockIdToTypeMap", "blockClassToBlockGroupMap", "blockGroupNames", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        shareable: typing.Union[MetaOapg.properties.shareable, bool, ],
        blockGroupNames: typing.Union[MetaOapg.properties.blockGroupNames, list, tuple, ],
        dataSchema: typing.Union[MetaOapg.properties.dataSchema, dict, frozendict.frozendict, ],
        simulationRequired: typing.Union[MetaOapg.properties.simulationRequired, bool, ],
        blockIdToTypeMap: typing.Union[MetaOapg.properties.blockIdToTypeMap, dict, frozendict.frozendict, ],
        data: 'VehicleTemplate',
        sharePwRqd: typing.Union[MetaOapg.properties.sharePwRqd, bool, ],
        dateModified: typing.Union[MetaOapg.properties.dateModified, str, datetime, ],
        repository: typing.Union[MetaOapg.properties.repository, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, ],
        mission: typing.Union[MetaOapg.properties.mission, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        numSimulations: typing.Union[MetaOapg.properties.numSimulations, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        user: typing.Union[MetaOapg.properties.user, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        blockClassToBlockGroupMap: typing.Union[MetaOapg.properties.blockClassToBlockGroupMap, dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BranchVehicleRes':
        return super().__new__(
            cls,
            *args,
            shareable=shareable,
            blockGroupNames=blockGroupNames,
            dataSchema=dataSchema,
            simulationRequired=simulationRequired,
            blockIdToTypeMap=blockIdToTypeMap,
            data=data,
            sharePwRqd=sharePwRqd,
            dateModified=dateModified,
            repository=repository,
            uuid=uuid,
            mission=mission,
            dateCreated=dateCreated,
            name=name,
            numSimulations=numSimulations,
            id=id,
            user=user,
            blockClassToBlockGroupMap=blockClassToBlockGroupMap,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.vehicle_template import VehicleTemplate
