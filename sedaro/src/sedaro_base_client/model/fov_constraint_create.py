# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com   # noqa: E501

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


class FOVConstraintCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "keepout",
            "fieldOfView",
            "name",
            "referenceVector",
            "destructive",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            keepout = schemas.BoolSchema
            destructive = schemas.BoolSchema
            referenceVector = schemas.StrSchema
            fieldOfView = schemas.StrSchema
            id = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "keepout": keepout,
                "destructive": destructive,
                "referenceVector": referenceVector,
                "fieldOfView": fieldOfView,
                "id": id,
            }
    
    keepout: MetaOapg.properties.keepout
    fieldOfView: MetaOapg.properties.fieldOfView
    name: MetaOapg.properties.name
    referenceVector: MetaOapg.properties.referenceVector
    destructive: MetaOapg.properties.destructive
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keepout"]) -> MetaOapg.properties.keepout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destructive"]) -> MetaOapg.properties.destructive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceVector"]) -> MetaOapg.properties.referenceVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldOfView"]) -> MetaOapg.properties.fieldOfView: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "keepout", "destructive", "referenceVector", "fieldOfView", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keepout"]) -> MetaOapg.properties.keepout: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destructive"]) -> MetaOapg.properties.destructive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceVector"]) -> MetaOapg.properties.referenceVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldOfView"]) -> MetaOapg.properties.fieldOfView: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "keepout", "destructive", "referenceVector", "fieldOfView", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        keepout: typing.Union[MetaOapg.properties.keepout, bool, ],
        fieldOfView: typing.Union[MetaOapg.properties.fieldOfView, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        referenceVector: typing.Union[MetaOapg.properties.referenceVector, str, ],
        destructive: typing.Union[MetaOapg.properties.destructive, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FOVConstraintCreate':
        return super().__new__(
            cls,
            *_args,
            keepout=keepout,
            fieldOfView=fieldOfView,
            name=name,
            referenceVector=referenceVector,
            destructive=destructive,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )
