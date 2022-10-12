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


class IROPolarCirc(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "initialRefOrbit",
            "nu",
            "alt",
            "raan",
        }
        
        class properties:
            
            
            class initialRefOrbit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "POLAR_CIRC": "POLAR_CIRC",
                    }
                
                @schemas.classproperty
                def POLAR_CIRC(cls):
                    return cls("POLAR_CIRC")
            
            
            class raan(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = 0.0
            
            
            class nu(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = 0.0
            
            
            class alt(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 100.0
            __annotations__ = {
                "initialRefOrbit": initialRefOrbit,
                "raan": raan,
                "nu": nu,
                "alt": alt,
            }
    
    initialRefOrbit: MetaOapg.properties.initialRefOrbit
    nu: MetaOapg.properties.nu
    alt: MetaOapg.properties.alt
    raan: MetaOapg.properties.raan
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialRefOrbit"]) -> MetaOapg.properties.initialRefOrbit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raan"]) -> MetaOapg.properties.raan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nu"]) -> MetaOapg.properties.nu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alt"]) -> MetaOapg.properties.alt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["initialRefOrbit", "raan", "nu", "alt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialRefOrbit"]) -> MetaOapg.properties.initialRefOrbit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raan"]) -> MetaOapg.properties.raan: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nu"]) -> MetaOapg.properties.nu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alt"]) -> MetaOapg.properties.alt: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["initialRefOrbit", "raan", "nu", "alt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        initialRefOrbit: typing.Union[MetaOapg.properties.initialRefOrbit, str, ],
        nu: typing.Union[MetaOapg.properties.nu, decimal.Decimal, int, float, ],
        alt: typing.Union[MetaOapg.properties.alt, decimal.Decimal, int, float, ],
        raan: typing.Union[MetaOapg.properties.raan, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IROPolarCirc':
        return super().__new__(
            cls,
            *args,
            initialRefOrbit=initialRefOrbit,
            nu=nu,
            alt=alt,
            raan=raan,
            _configuration=_configuration,
            **kwargs,
        )
