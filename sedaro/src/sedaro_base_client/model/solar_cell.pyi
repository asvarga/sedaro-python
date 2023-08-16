# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.5.2
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


class SolarCell(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "maxPowerCurrent",
            "shortCircuitCurrent",
            "numJunctions",
            "maxPowerVoltage",
            "openCircuitVoltage",
        }
        
        class properties:
            openCircuitVoltage = schemas.NumberSchema
            shortCircuitCurrent = schemas.NumberSchema
            maxPowerVoltage = schemas.NumberSchema
            maxPowerCurrent = schemas.NumberSchema
            
            
            class numJunctions(
                schemas.IntSchema
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
            __annotations__ = {
                "openCircuitVoltage": openCircuitVoltage,
                "shortCircuitCurrent": shortCircuitCurrent,
                "maxPowerVoltage": maxPowerVoltage,
                "maxPowerCurrent": maxPowerCurrent,
                "numJunctions": numJunctions,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    maxPowerCurrent: MetaOapg.properties.maxPowerCurrent
    shortCircuitCurrent: MetaOapg.properties.shortCircuitCurrent
    numJunctions: MetaOapg.properties.numJunctions
    maxPowerVoltage: MetaOapg.properties.maxPowerVoltage
    openCircuitVoltage: MetaOapg.properties.openCircuitVoltage
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPowerCurrent"]) -> MetaOapg.properties.maxPowerCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortCircuitCurrent"]) -> MetaOapg.properties.shortCircuitCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numJunctions"]) -> MetaOapg.properties.numJunctions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPowerVoltage"]) -> MetaOapg.properties.maxPowerVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["openCircuitVoltage"]) -> MetaOapg.properties.openCircuitVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer"]) -> MetaOapg.properties.manufacturer: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxPowerCurrent"], typing_extensions.Literal["shortCircuitCurrent"], typing_extensions.Literal["numJunctions"], typing_extensions.Literal["maxPowerVoltage"], typing_extensions.Literal["openCircuitVoltage"], typing_extensions.Literal["id"], typing_extensions.Literal["partNumber"], typing_extensions.Literal["manufacturer"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPowerCurrent"]) -> MetaOapg.properties.maxPowerCurrent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortCircuitCurrent"]) -> MetaOapg.properties.shortCircuitCurrent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numJunctions"]) -> MetaOapg.properties.numJunctions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPowerVoltage"]) -> MetaOapg.properties.maxPowerVoltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["openCircuitVoltage"]) -> MetaOapg.properties.openCircuitVoltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partNumber"]) -> typing.Union[MetaOapg.properties.partNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer"]) -> typing.Union[MetaOapg.properties.manufacturer, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxPowerCurrent"], typing_extensions.Literal["shortCircuitCurrent"], typing_extensions.Literal["numJunctions"], typing_extensions.Literal["maxPowerVoltage"], typing_extensions.Literal["openCircuitVoltage"], typing_extensions.Literal["id"], typing_extensions.Literal["partNumber"], typing_extensions.Literal["manufacturer"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxPowerCurrent: typing.Union[MetaOapg.properties.maxPowerCurrent, decimal.Decimal, int, float, ],
        shortCircuitCurrent: typing.Union[MetaOapg.properties.shortCircuitCurrent, decimal.Decimal, int, float, ],
        numJunctions: typing.Union[MetaOapg.properties.numJunctions, decimal.Decimal, int, ],
        maxPowerVoltage: typing.Union[MetaOapg.properties.maxPowerVoltage, decimal.Decimal, int, float, ],
        openCircuitVoltage: typing.Union[MetaOapg.properties.openCircuitVoltage, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SolarCell':
        return super().__new__(
            cls,
            *_args,
            maxPowerCurrent=maxPowerCurrent,
            shortCircuitCurrent=shortCircuitCurrent,
            numJunctions=numJunctions,
            maxPowerVoltage=maxPowerVoltage,
            openCircuitVoltage=openCircuitVoltage,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            _configuration=_configuration,
        )
