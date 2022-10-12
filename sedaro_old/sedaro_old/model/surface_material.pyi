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


class SurfaceMaterial(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "hotTempRating",
            "diffuseSolarReflectivity",
            "specularSolarReflectivity",
            "solarAbsorptivity",
            "coldTempRating",
            "irEmissivity",
        }
        
        class properties:
            
            
            class irEmissivity(
                schemas.NumberSchema
            ):
                pass
            
            
            class solarAbsorptivity(
                schemas.NumberSchema
            ):
                pass
            
            
            class diffuseSolarReflectivity(
                schemas.NumberSchema
            ):
                pass
            
            
            class specularSolarReflectivity(
                schemas.NumberSchema
            ):
                pass
            hotTempRating = schemas.NumberSchema
            coldTempRating = schemas.NumberSchema
            id = schemas.StrSchema
            
            
            class partNumber(
                schemas.StrSchema
            ):
                pass
            
            
            class manufacturer(
                schemas.StrSchema
            ):
                pass
            
            
            class surfaces(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'surfaces':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "irEmissivity": irEmissivity,
                "solarAbsorptivity": solarAbsorptivity,
                "diffuseSolarReflectivity": diffuseSolarReflectivity,
                "specularSolarReflectivity": specularSolarReflectivity,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "surfaces": surfaces,
            }
    
    hotTempRating: MetaOapg.properties.hotTempRating
    diffuseSolarReflectivity: MetaOapg.properties.diffuseSolarReflectivity
    specularSolarReflectivity: MetaOapg.properties.specularSolarReflectivity
    solarAbsorptivity: MetaOapg.properties.solarAbsorptivity
    coldTempRating: MetaOapg.properties.coldTempRating
    irEmissivity: MetaOapg.properties.irEmissivity
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["irEmissivity"]) -> MetaOapg.properties.irEmissivity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["solarAbsorptivity"]) -> MetaOapg.properties.solarAbsorptivity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["diffuseSolarReflectivity"]) -> MetaOapg.properties.diffuseSolarReflectivity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["specularSolarReflectivity"]) -> MetaOapg.properties.specularSolarReflectivity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotTempRating"]) -> MetaOapg.properties.hotTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldTempRating"]) -> MetaOapg.properties.coldTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer"]) -> MetaOapg.properties.manufacturer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaces"]) -> MetaOapg.properties.surfaces: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["irEmissivity", "solarAbsorptivity", "diffuseSolarReflectivity", "specularSolarReflectivity", "hotTempRating", "coldTempRating", "id", "partNumber", "manufacturer", "surfaces", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["irEmissivity"]) -> MetaOapg.properties.irEmissivity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["solarAbsorptivity"]) -> MetaOapg.properties.solarAbsorptivity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["diffuseSolarReflectivity"]) -> MetaOapg.properties.diffuseSolarReflectivity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["specularSolarReflectivity"]) -> MetaOapg.properties.specularSolarReflectivity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotTempRating"]) -> MetaOapg.properties.hotTempRating: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldTempRating"]) -> MetaOapg.properties.coldTempRating: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partNumber"]) -> typing.Union[MetaOapg.properties.partNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer"]) -> typing.Union[MetaOapg.properties.manufacturer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaces"]) -> typing.Union[MetaOapg.properties.surfaces, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["irEmissivity", "solarAbsorptivity", "diffuseSolarReflectivity", "specularSolarReflectivity", "hotTempRating", "coldTempRating", "id", "partNumber", "manufacturer", "surfaces", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, ],
        diffuseSolarReflectivity: typing.Union[MetaOapg.properties.diffuseSolarReflectivity, decimal.Decimal, int, float, ],
        specularSolarReflectivity: typing.Union[MetaOapg.properties.specularSolarReflectivity, decimal.Decimal, int, float, ],
        solarAbsorptivity: typing.Union[MetaOapg.properties.solarAbsorptivity, decimal.Decimal, int, float, ],
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, ],
        irEmissivity: typing.Union[MetaOapg.properties.irEmissivity, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        surfaces: typing.Union[MetaOapg.properties.surfaces, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SurfaceMaterial':
        return super().__new__(
            cls,
            *args,
            hotTempRating=hotTempRating,
            diffuseSolarReflectivity=diffuseSolarReflectivity,
            specularSolarReflectivity=specularSolarReflectivity,
            solarAbsorptivity=solarAbsorptivity,
            coldTempRating=coldTempRating,
            irEmissivity=irEmissivity,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            surfaces=surfaces,
            _configuration=_configuration,
            **kwargs,
        )
