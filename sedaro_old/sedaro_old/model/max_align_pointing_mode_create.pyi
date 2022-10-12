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

from sedaro_old import schemas  # noqa: F401


class MaxAlignPointingModeCreate(
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
            "maxAlignVector",
            "pointingModeType",
            "lockVector",
            "acAlgorithm",
            "conOps",
            "maxAlignBodyFrameVector",
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
                def MAX_SECONDARY_ALIGN(cls):
                    return cls("MAX_SECONDARY_ALIGN")
            conOps = schemas.StrSchema
            lockVector = schemas.StrSchema
            lockBodyFrameVector = schemas.StrSchema
            acAlgorithm = schemas.StrSchema
            maxAlignVector = schemas.StrSchema
            maxAlignBodyFrameVector = schemas.StrSchema
            id = schemas.StrSchema
            odAlgorithm = schemas.StrSchema
            adAlgorithm = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "pointingModeType": pointingModeType,
                "conOps": conOps,
                "lockVector": lockVector,
                "lockBodyFrameVector": lockBodyFrameVector,
                "acAlgorithm": acAlgorithm,
                "maxAlignVector": maxAlignVector,
                "maxAlignBodyFrameVector": maxAlignBodyFrameVector,
                "id": id,
                "odAlgorithm": odAlgorithm,
                "adAlgorithm": adAlgorithm,
            }
    
    lockBodyFrameVector: MetaOapg.properties.lockBodyFrameVector
    name: MetaOapg.properties.name
    maxAlignVector: MetaOapg.properties.maxAlignVector
    pointingModeType: MetaOapg.properties.pointingModeType
    lockVector: MetaOapg.properties.lockVector
    acAlgorithm: MetaOapg.properties.acAlgorithm
    conOps: MetaOapg.properties.conOps
    maxAlignBodyFrameVector: MetaOapg.properties.maxAlignBodyFrameVector
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockVector"]) -> MetaOapg.properties.lockVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> MetaOapg.properties.lockBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acAlgorithm"]) -> MetaOapg.properties.acAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxAlignVector"]) -> MetaOapg.properties.maxAlignVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxAlignBodyFrameVector"]) -> MetaOapg.properties.maxAlignBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["odAlgorithm"]) -> MetaOapg.properties.odAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adAlgorithm"]) -> MetaOapg.properties.adAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "conOps", "lockVector", "lockBodyFrameVector", "acAlgorithm", "maxAlignVector", "maxAlignBodyFrameVector", "id", "odAlgorithm", "adAlgorithm", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockVector"]) -> MetaOapg.properties.lockVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> MetaOapg.properties.lockBodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acAlgorithm"]) -> MetaOapg.properties.acAlgorithm: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxAlignVector"]) -> MetaOapg.properties.maxAlignVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxAlignBodyFrameVector"]) -> MetaOapg.properties.maxAlignBodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["odAlgorithm"]) -> typing.Union[MetaOapg.properties.odAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adAlgorithm"]) -> typing.Union[MetaOapg.properties.adAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "conOps", "lockVector", "lockBodyFrameVector", "acAlgorithm", "maxAlignVector", "maxAlignBodyFrameVector", "id", "odAlgorithm", "adAlgorithm", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lockBodyFrameVector: typing.Union[MetaOapg.properties.lockBodyFrameVector, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        maxAlignVector: typing.Union[MetaOapg.properties.maxAlignVector, str, ],
        pointingModeType: typing.Union[MetaOapg.properties.pointingModeType, str, ],
        lockVector: typing.Union[MetaOapg.properties.lockVector, str, ],
        acAlgorithm: typing.Union[MetaOapg.properties.acAlgorithm, str, ],
        conOps: typing.Union[MetaOapg.properties.conOps, str, ],
        maxAlignBodyFrameVector: typing.Union[MetaOapg.properties.maxAlignBodyFrameVector, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        odAlgorithm: typing.Union[MetaOapg.properties.odAlgorithm, str, schemas.Unset] = schemas.unset,
        adAlgorithm: typing.Union[MetaOapg.properties.adAlgorithm, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MaxAlignPointingModeCreate':
        return super().__new__(
            cls,
            *args,
            lockBodyFrameVector=lockBodyFrameVector,
            name=name,
            maxAlignVector=maxAlignVector,
            pointingModeType=pointingModeType,
            lockVector=lockVector,
            acAlgorithm=acAlgorithm,
            conOps=conOps,
            maxAlignBodyFrameVector=maxAlignBodyFrameVector,
            id=id,
            odAlgorithm=odAlgorithm,
            adAlgorithm=adAlgorithm,
            _configuration=_configuration,
            **kwargs,
        )
