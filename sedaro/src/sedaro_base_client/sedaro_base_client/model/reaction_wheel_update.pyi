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


class ReactionWheelUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "bodyFrameVector",
            "efficiency",
            "inertia",
            "ratedTorque",
            "name",
            "ratedMomentum",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            bodyFrameVector = schemas.StrSchema
            
            
            class inertia(
                schemas.NumberSchema
            ):
                pass
            
            
            class ratedMomentum(
                schemas.NumberSchema
            ):
                pass
            
            
            class ratedTorque(
                schemas.NumberSchema
            ):
                pass
            
            
            class efficiency(
                schemas.NumberSchema
            ):
                pass
            id = schemas.StrSchema
            
            
            class partNumber(
                schemas.StrSchema
            ):
                pass
            
            
            class manufacturer(
                schemas.StrSchema
            ):
                pass
            hotTempRating = schemas.NumberSchema
            coldTempRating = schemas.NumberSchema
            
            
            class thermalCapacitance(
                schemas.NumberSchema
            ):
                pass
            temperature = schemas.NumberSchema
            __annotations__ = {
                "name": name,
                "bodyFrameVector": bodyFrameVector,
                "inertia": inertia,
                "ratedMomentum": ratedMomentum,
                "ratedTorque": ratedTorque,
                "efficiency": efficiency,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
                "thermalCapacitance": thermalCapacitance,
                "temperature": temperature,
            }
    
    bodyFrameVector: MetaOapg.properties.bodyFrameVector
    efficiency: MetaOapg.properties.efficiency
    inertia: MetaOapg.properties.inertia
    ratedTorque: MetaOapg.properties.ratedTorque
    name: MetaOapg.properties.name
    ratedMomentum: MetaOapg.properties.ratedMomentum
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inertia"]) -> MetaOapg.properties.inertia: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratedMomentum"]) -> MetaOapg.properties.ratedMomentum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratedTorque"]) -> MetaOapg.properties.ratedTorque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["efficiency"]) -> MetaOapg.properties.efficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer"]) -> MetaOapg.properties.manufacturer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotTempRating"]) -> MetaOapg.properties.hotTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldTempRating"]) -> MetaOapg.properties.coldTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermalCapacitance"]) -> MetaOapg.properties.thermalCapacitance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "bodyFrameVector", "inertia", "ratedMomentum", "ratedTorque", "efficiency", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "temperature", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inertia"]) -> MetaOapg.properties.inertia: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratedMomentum"]) -> MetaOapg.properties.ratedMomentum: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratedTorque"]) -> MetaOapg.properties.ratedTorque: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["efficiency"]) -> MetaOapg.properties.efficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partNumber"]) -> typing.Union[MetaOapg.properties.partNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer"]) -> typing.Union[MetaOapg.properties.manufacturer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotTempRating"]) -> typing.Union[MetaOapg.properties.hotTempRating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldTempRating"]) -> typing.Union[MetaOapg.properties.coldTempRating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermalCapacitance"]) -> typing.Union[MetaOapg.properties.thermalCapacitance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> typing.Union[MetaOapg.properties.temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "bodyFrameVector", "inertia", "ratedMomentum", "ratedTorque", "efficiency", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "temperature", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bodyFrameVector: typing.Union[MetaOapg.properties.bodyFrameVector, str, ],
        efficiency: typing.Union[MetaOapg.properties.efficiency, decimal.Decimal, int, float, ],
        inertia: typing.Union[MetaOapg.properties.inertia, decimal.Decimal, int, float, ],
        ratedTorque: typing.Union[MetaOapg.properties.ratedTorque, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        ratedMomentum: typing.Union[MetaOapg.properties.ratedMomentum, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        thermalCapacitance: typing.Union[MetaOapg.properties.thermalCapacitance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReactionWheelUpdate':
        return super().__new__(
            cls,
            *args,
            bodyFrameVector=bodyFrameVector,
            efficiency=efficiency,
            inertia=inertia,
            ratedTorque=ratedTorque,
            name=name,
            ratedMomentum=ratedMomentum,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            hotTempRating=hotTempRating,
            coldTempRating=coldTempRating,
            thermalCapacitance=thermalCapacitance,
            temperature=temperature,
            _configuration=_configuration,
            **kwargs,
        )
