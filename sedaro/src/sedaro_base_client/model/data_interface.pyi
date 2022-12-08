# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.4
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


class DataInterface(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "onBitRate",
            "bus",
            "sink",
            "dataType",
            "name",
            "source",
            "alwaysActive",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            dataType = schemas.StrSchema
            onBitRate = schemas.IntSchema
            alwaysActive = schemas.BoolSchema
            source = schemas.StrSchema
            sink = schemas.StrSchema
            bus = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class opModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'opModes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class bitRate(
                schemas.IntSchema
            ):
                pass
            isActive = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "dataType": dataType,
                "onBitRate": onBitRate,
                "alwaysActive": alwaysActive,
                "source": source,
                "sink": sink,
                "bus": bus,
                "id": id,
                "opModes": opModes,
                "bitRate": bitRate,
                "isActive": isActive,
            }
    
    onBitRate: MetaOapg.properties.onBitRate
    bus: MetaOapg.properties.bus
    sink: MetaOapg.properties.sink
    dataType: MetaOapg.properties.dataType
    name: MetaOapg.properties.name
    source: MetaOapg.properties.source
    alwaysActive: MetaOapg.properties.alwaysActive
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataType"]) -> MetaOapg.properties.dataType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onBitRate"]) -> MetaOapg.properties.onBitRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alwaysActive"]) -> MetaOapg.properties.alwaysActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sink"]) -> MetaOapg.properties.sink: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bus"]) -> MetaOapg.properties.bus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opModes"]) -> MetaOapg.properties.opModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bitRate"]) -> MetaOapg.properties.bitRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "dataType", "onBitRate", "alwaysActive", "source", "sink", "bus", "id", "opModes", "bitRate", "isActive", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataType"]) -> MetaOapg.properties.dataType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onBitRate"]) -> MetaOapg.properties.onBitRate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alwaysActive"]) -> MetaOapg.properties.alwaysActive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sink"]) -> MetaOapg.properties.sink: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bus"]) -> MetaOapg.properties.bus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opModes"]) -> typing.Union[MetaOapg.properties.opModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bitRate"]) -> typing.Union[MetaOapg.properties.bitRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "dataType", "onBitRate", "alwaysActive", "source", "sink", "bus", "id", "opModes", "bitRate", "isActive", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        onBitRate: typing.Union[MetaOapg.properties.onBitRate, decimal.Decimal, int, ],
        bus: typing.Union[MetaOapg.properties.bus, str, ],
        sink: typing.Union[MetaOapg.properties.sink, str, ],
        dataType: typing.Union[MetaOapg.properties.dataType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        source: typing.Union[MetaOapg.properties.source, str, ],
        alwaysActive: typing.Union[MetaOapg.properties.alwaysActive, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        opModes: typing.Union[MetaOapg.properties.opModes, list, tuple, schemas.Unset] = schemas.unset,
        bitRate: typing.Union[MetaOapg.properties.bitRate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataInterface':
        return super().__new__(
            cls,
            *_args,
            onBitRate=onBitRate,
            bus=bus,
            sink=sink,
            dataType=dataType,
            name=name,
            source=source,
            alwaysActive=alwaysActive,
            id=id,
            opModes=opModes,
            bitRate=bitRate,
            isActive=isActive,
            _configuration=_configuration,
            **kwargs,
        )
