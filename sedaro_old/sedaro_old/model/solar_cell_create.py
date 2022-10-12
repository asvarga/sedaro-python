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


class SolarCellCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "maxPowerCurrent",
            "topology",
            "shortCircuitCurrent",
            "numJunctions",
            "maxPowerVoltage",
            "openCircuitVoltage",
        }
        
        class properties:
            
            
            class openCircuitVoltage(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class shortCircuitCurrent(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class maxPowerVoltage(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class maxPowerCurrent(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class numJunctions(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 1
            topology = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class partNumber(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            
            
            class manufacturer(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            __annotations__ = {
                "openCircuitVoltage": openCircuitVoltage,
                "shortCircuitCurrent": shortCircuitCurrent,
                "maxPowerVoltage": maxPowerVoltage,
                "maxPowerCurrent": maxPowerCurrent,
                "numJunctions": numJunctions,
                "topology": topology,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
            }
    
    maxPowerCurrent: MetaOapg.properties.maxPowerCurrent
    topology: MetaOapg.properties.topology
    shortCircuitCurrent: MetaOapg.properties.shortCircuitCurrent
    numJunctions: MetaOapg.properties.numJunctions
    maxPowerVoltage: MetaOapg.properties.maxPowerVoltage
    openCircuitVoltage: MetaOapg.properties.openCircuitVoltage
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["openCircuitVoltage"]) -> MetaOapg.properties.openCircuitVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortCircuitCurrent"]) -> MetaOapg.properties.shortCircuitCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPowerVoltage"]) -> MetaOapg.properties.maxPowerVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPowerCurrent"]) -> MetaOapg.properties.maxPowerCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numJunctions"]) -> MetaOapg.properties.numJunctions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer"]) -> MetaOapg.properties.manufacturer: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["openCircuitVoltage", "shortCircuitCurrent", "maxPowerVoltage", "maxPowerCurrent", "numJunctions", "topology", "id", "partNumber", "manufacturer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["openCircuitVoltage"]) -> MetaOapg.properties.openCircuitVoltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortCircuitCurrent"]) -> MetaOapg.properties.shortCircuitCurrent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPowerVoltage"]) -> MetaOapg.properties.maxPowerVoltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPowerCurrent"]) -> MetaOapg.properties.maxPowerCurrent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numJunctions"]) -> MetaOapg.properties.numJunctions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partNumber"]) -> typing.Union[MetaOapg.properties.partNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer"]) -> typing.Union[MetaOapg.properties.manufacturer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["openCircuitVoltage", "shortCircuitCurrent", "maxPowerVoltage", "maxPowerCurrent", "numJunctions", "topology", "id", "partNumber", "manufacturer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        maxPowerCurrent: typing.Union[MetaOapg.properties.maxPowerCurrent, decimal.Decimal, int, float, ],
        topology: typing.Union[MetaOapg.properties.topology, str, ],
        shortCircuitCurrent: typing.Union[MetaOapg.properties.shortCircuitCurrent, decimal.Decimal, int, float, ],
        numJunctions: typing.Union[MetaOapg.properties.numJunctions, decimal.Decimal, int, ],
        maxPowerVoltage: typing.Union[MetaOapg.properties.maxPowerVoltage, decimal.Decimal, int, float, ],
        openCircuitVoltage: typing.Union[MetaOapg.properties.openCircuitVoltage, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SolarCellCreate':
        return super().__new__(
            cls,
            *args,
            maxPowerCurrent=maxPowerCurrent,
            topology=topology,
            shortCircuitCurrent=shortCircuitCurrent,
            numJunctions=numJunctions,
            maxPowerVoltage=maxPowerVoltage,
            openCircuitVoltage=openCircuitVoltage,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            _configuration=_configuration,
            **kwargs,
        )
