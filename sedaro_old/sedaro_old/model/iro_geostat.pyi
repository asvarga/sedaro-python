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


class IROGeostat(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "initialRefOrbit",
            "lon",
        }
        
        class properties:
            
            
            class initialRefOrbit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GEOSTAT(cls):
                    return cls("GEOSTAT")
            
            
            class lon(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "initialRefOrbit": initialRefOrbit,
                "lon": lon,
            }
    
    initialRefOrbit: MetaOapg.properties.initialRefOrbit
    lon: MetaOapg.properties.lon
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialRefOrbit"]) -> MetaOapg.properties.initialRefOrbit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lon"]) -> MetaOapg.properties.lon: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["initialRefOrbit", "lon", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialRefOrbit"]) -> MetaOapg.properties.initialRefOrbit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lon"]) -> MetaOapg.properties.lon: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["initialRefOrbit", "lon", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        initialRefOrbit: typing.Union[MetaOapg.properties.initialRefOrbit, str, ],
        lon: typing.Union[MetaOapg.properties.lon, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IROGeostat':
        return super().__new__(
            cls,
            *args,
            initialRefOrbit=initialRefOrbit,
            lon=lon,
            _configuration=_configuration,
            **kwargs,
        )
