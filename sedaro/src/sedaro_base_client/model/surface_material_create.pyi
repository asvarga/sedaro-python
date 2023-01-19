# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the  Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests  via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised,  you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.6
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


class SurfaceMaterialCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited only by `Collection` and `Block`. Adds helper methods that help with
relationship fields.
    """


    class MetaOapg:
        required = {
            "diffuseSolarReflectivity",
            "specularSolarReflectivity",
            "solarAbsorptivity",
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
            id = schemas.StrSchema
            
            
            class partNumber(
                schemas.StrSchema
            ):
                pass
            
            
            class manufacturer(
                schemas.StrSchema
            ):
                pass
            
            
            class hotTempRating(
                schemas.NumberSchema
            ):
                pass
            
            
            class coldTempRating(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "irEmissivity": irEmissivity,
                "solarAbsorptivity": solarAbsorptivity,
                "diffuseSolarReflectivity": diffuseSolarReflectivity,
                "specularSolarReflectivity": specularSolarReflectivity,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
            }
    
    diffuseSolarReflectivity: MetaOapg.properties.diffuseSolarReflectivity
    specularSolarReflectivity: MetaOapg.properties.specularSolarReflectivity
    solarAbsorptivity: MetaOapg.properties.solarAbsorptivity
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
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["irEmissivity", "solarAbsorptivity", "diffuseSolarReflectivity", "specularSolarReflectivity", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", ], str]):
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
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["irEmissivity", "solarAbsorptivity", "diffuseSolarReflectivity", "specularSolarReflectivity", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        diffuseSolarReflectivity: typing.Union[MetaOapg.properties.diffuseSolarReflectivity, decimal.Decimal, int, float, ],
        specularSolarReflectivity: typing.Union[MetaOapg.properties.specularSolarReflectivity, decimal.Decimal, int, float, ],
        solarAbsorptivity: typing.Union[MetaOapg.properties.solarAbsorptivity, decimal.Decimal, int, float, ],
        irEmissivity: typing.Union[MetaOapg.properties.irEmissivity, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SurfaceMaterialCreate':
        return super().__new__(
            cls,
            *_args,
            diffuseSolarReflectivity=diffuseSolarReflectivity,
            specularSolarReflectivity=specularSolarReflectivity,
            solarAbsorptivity=solarAbsorptivity,
            irEmissivity=irEmissivity,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            hotTempRating=hotTempRating,
            coldTempRating=coldTempRating,
            _configuration=_configuration,
            **kwargs,
        )
