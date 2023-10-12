# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.7.0
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


class FuelReservoir(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A FuelReservoir Block
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            id = schemas.StrSchema
            
            
            class fuelTanks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fuelTanks':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class thrusters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thrusters':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class flowRate(
                schemas.NumberSchema
            ):
                pass
            
            
            class totalFuel(
                schemas.NumberSchema
            ):
                pass
            
            
            class fillPercent(
                schemas.NumberSchema
            ):
                pass
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FUEL_RESERVOIR(cls):
                    return cls("FuelReservoir")
            __annotations__ = {
                "name": name,
                "id": id,
                "fuelTanks": fuelTanks,
                "thrusters": thrusters,
                "flowRate": flowRate,
                "totalFuel": totalFuel,
                "fillPercent": fillPercent,
                "type": type,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fuelTanks"]) -> MetaOapg.properties.fuelTanks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thrusters"]) -> MetaOapg.properties.thrusters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flowRate"]) -> MetaOapg.properties.flowRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalFuel"]) -> MetaOapg.properties.totalFuel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fillPercent"]) -> MetaOapg.properties.fillPercent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["fuelTanks"], typing_extensions.Literal["thrusters"], typing_extensions.Literal["flowRate"], typing_extensions.Literal["totalFuel"], typing_extensions.Literal["fillPercent"], typing_extensions.Literal["type"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fuelTanks"]) -> typing.Union[MetaOapg.properties.fuelTanks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thrusters"]) -> typing.Union[MetaOapg.properties.thrusters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flowRate"]) -> typing.Union[MetaOapg.properties.flowRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalFuel"]) -> typing.Union[MetaOapg.properties.totalFuel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fillPercent"]) -> typing.Union[MetaOapg.properties.fillPercent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["fuelTanks"], typing_extensions.Literal["thrusters"], typing_extensions.Literal["flowRate"], typing_extensions.Literal["totalFuel"], typing_extensions.Literal["fillPercent"], typing_extensions.Literal["type"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        fuelTanks: typing.Union[MetaOapg.properties.fuelTanks, list, tuple, schemas.Unset] = schemas.unset,
        thrusters: typing.Union[MetaOapg.properties.thrusters, list, tuple, schemas.Unset] = schemas.unset,
        flowRate: typing.Union[MetaOapg.properties.flowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalFuel: typing.Union[MetaOapg.properties.totalFuel, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fillPercent: typing.Union[MetaOapg.properties.fillPercent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FuelReservoir':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            fuelTanks=fuelTanks,
            thrusters=thrusters,
            flowRate=flowRate,
            totalFuel=totalFuel,
            fillPercent=fillPercent,
            type=type,
            _configuration=_configuration,
        )
