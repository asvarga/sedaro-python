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


class SlidingModeAlgorithm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "epsilon",
            "gainG",
            "algorithmType",
            "gainK",
            "rate",
            "name",
            "algorithmSubtype",
            "gainC",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            rate = schemas.NumberSchema
            
            
            class algorithmType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ATTITUDE_CONTROL": "ATTITUDE_CONTROL",
                    }
                
                @schemas.classproperty
                def ATTITUDE_CONTROL(cls):
                    return cls("ATTITUDE_CONTROL")
            
            
            class algorithmSubtype(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SLIDING_MODE": "SLIDING_MODE",
                    }
                
                @schemas.classproperty
                def SLIDING_MODE(cls):
                    return cls("SLIDING_MODE")
            gainK = schemas.NumberSchema
            gainG = schemas.NumberSchema
            gainC = schemas.NumberSchema
            epsilon = schemas.NumberSchema
            id = schemas.StrSchema
            
            
            class actuators(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actuators':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "rate": rate,
                "algorithmType": algorithmType,
                "algorithmSubtype": algorithmSubtype,
                "gainK": gainK,
                "gainG": gainG,
                "gainC": gainC,
                "epsilon": epsilon,
                "id": id,
                "actuators": actuators,
            }
    
    epsilon: MetaOapg.properties.epsilon
    gainG: MetaOapg.properties.gainG
    algorithmType: MetaOapg.properties.algorithmType
    gainK: MetaOapg.properties.gainK
    rate: MetaOapg.properties.rate
    name: MetaOapg.properties.name
    algorithmSubtype: MetaOapg.properties.algorithmSubtype
    gainC: MetaOapg.properties.gainC
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainK"]) -> MetaOapg.properties.gainK: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainG"]) -> MetaOapg.properties.gainG: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainC"]) -> MetaOapg.properties.gainC: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["epsilon"]) -> MetaOapg.properties.epsilon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actuators"]) -> MetaOapg.properties.actuators: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "gainK", "gainG", "gainC", "epsilon", "id", "actuators", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainK"]) -> MetaOapg.properties.gainK: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainG"]) -> MetaOapg.properties.gainG: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainC"]) -> MetaOapg.properties.gainC: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["epsilon"]) -> MetaOapg.properties.epsilon: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actuators"]) -> typing.Union[MetaOapg.properties.actuators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "gainK", "gainG", "gainC", "epsilon", "id", "actuators", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        epsilon: typing.Union[MetaOapg.properties.epsilon, decimal.Decimal, int, float, ],
        gainG: typing.Union[MetaOapg.properties.gainG, decimal.Decimal, int, float, ],
        algorithmType: typing.Union[MetaOapg.properties.algorithmType, str, ],
        gainK: typing.Union[MetaOapg.properties.gainK, decimal.Decimal, int, float, ],
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        algorithmSubtype: typing.Union[MetaOapg.properties.algorithmSubtype, str, ],
        gainC: typing.Union[MetaOapg.properties.gainC, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        actuators: typing.Union[MetaOapg.properties.actuators, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SlidingModeAlgorithm':
        return super().__new__(
            cls,
            *args,
            epsilon=epsilon,
            gainG=gainG,
            algorithmType=algorithmType,
            gainK=gainK,
            rate=rate,
            name=name,
            algorithmSubtype=algorithmSubtype,
            gainC=gainC,
            id=id,
            actuators=actuators,
            _configuration=_configuration,
            **kwargs,
        )
