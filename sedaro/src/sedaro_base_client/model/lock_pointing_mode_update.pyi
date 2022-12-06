# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.2.12
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


class LockPointingModeUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "lockBodyFrameVector",
            "name",
            "pointingModeType",
            "acAlgorithm",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class pointingModeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LOCK(cls):
                    return cls("LOCK")
            lockBodyFrameVector = schemas.StrSchema
            acAlgorithm = schemas.StrSchema
            id = schemas.StrSchema
            odAlgorithm = schemas.StrSchema
            adAlgorithm = schemas.StrSchema
            lockVector = schemas.StrSchema
            spinRate = schemas.NumberSchema
            __annotations__ = {
                "name": name,
                "pointingModeType": pointingModeType,
                "lockBodyFrameVector": lockBodyFrameVector,
                "acAlgorithm": acAlgorithm,
                "id": id,
                "odAlgorithm": odAlgorithm,
                "adAlgorithm": adAlgorithm,
                "lockVector": lockVector,
                "spinRate": spinRate,
            }
    
    lockBodyFrameVector: MetaOapg.properties.lockBodyFrameVector
    name: MetaOapg.properties.name
    pointingModeType: MetaOapg.properties.pointingModeType
    acAlgorithm: MetaOapg.properties.acAlgorithm
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> MetaOapg.properties.lockBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acAlgorithm"]) -> MetaOapg.properties.acAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["odAlgorithm"]) -> MetaOapg.properties.odAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adAlgorithm"]) -> MetaOapg.properties.adAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockVector"]) -> MetaOapg.properties.lockVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spinRate"]) -> MetaOapg.properties.spinRate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "lockBodyFrameVector", "acAlgorithm", "id", "odAlgorithm", "adAlgorithm", "lockVector", "spinRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> MetaOapg.properties.lockBodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acAlgorithm"]) -> MetaOapg.properties.acAlgorithm: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["odAlgorithm"]) -> typing.Union[MetaOapg.properties.odAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adAlgorithm"]) -> typing.Union[MetaOapg.properties.adAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockVector"]) -> typing.Union[MetaOapg.properties.lockVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spinRate"]) -> typing.Union[MetaOapg.properties.spinRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "lockBodyFrameVector", "acAlgorithm", "id", "odAlgorithm", "adAlgorithm", "lockVector", "spinRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        lockBodyFrameVector: typing.Union[MetaOapg.properties.lockBodyFrameVector, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        pointingModeType: typing.Union[MetaOapg.properties.pointingModeType, str, ],
        acAlgorithm: typing.Union[MetaOapg.properties.acAlgorithm, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        odAlgorithm: typing.Union[MetaOapg.properties.odAlgorithm, str, schemas.Unset] = schemas.unset,
        adAlgorithm: typing.Union[MetaOapg.properties.adAlgorithm, str, schemas.Unset] = schemas.unset,
        lockVector: typing.Union[MetaOapg.properties.lockVector, str, schemas.Unset] = schemas.unset,
        spinRate: typing.Union[MetaOapg.properties.spinRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LockPointingModeUpdate':
        return super().__new__(
            cls,
            *_args,
            lockBodyFrameVector=lockBodyFrameVector,
            name=name,
            pointingModeType=pointingModeType,
            acAlgorithm=acAlgorithm,
            id=id,
            odAlgorithm=odAlgorithm,
            adAlgorithm=adAlgorithm,
            lockVector=lockVector,
            spinRate=spinRate,
            _configuration=_configuration,
            **kwargs,
        )
