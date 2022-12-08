# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.4
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


class SolarArray(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "topology",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            topology = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class panels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'panels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            idealOpenCircuitVoltage = schemas.NumberSchema
            idealShortCircuitCurrent = schemas.NumberSchema
            current = schemas.NumberSchema
            voltage = schemas.NumberSchema
            maxPower = schemas.NumberSchema
            maxPowerVoltage = schemas.NumberSchema
            maxPowerCurrent = schemas.NumberSchema
            openCircuitVoltage = schemas.NumberSchema
            power = schemas.NumberSchema
            
            
            class utilization(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "topology": topology,
                "id": id,
                "panels": panels,
                "idealOpenCircuitVoltage": idealOpenCircuitVoltage,
                "idealShortCircuitCurrent": idealShortCircuitCurrent,
                "current": current,
                "voltage": voltage,
                "maxPower": maxPower,
                "maxPowerVoltage": maxPowerVoltage,
                "maxPowerCurrent": maxPowerCurrent,
                "openCircuitVoltage": openCircuitVoltage,
                "power": power,
                "utilization": utilization,
            }
    
    topology: MetaOapg.properties.topology
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["panels"]) -> MetaOapg.properties.panels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idealOpenCircuitVoltage"]) -> MetaOapg.properties.idealOpenCircuitVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idealShortCircuitCurrent"]) -> MetaOapg.properties.idealShortCircuitCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voltage"]) -> MetaOapg.properties.voltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPower"]) -> MetaOapg.properties.maxPower: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPowerVoltage"]) -> MetaOapg.properties.maxPowerVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPowerCurrent"]) -> MetaOapg.properties.maxPowerCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["openCircuitVoltage"]) -> MetaOapg.properties.openCircuitVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["power"]) -> MetaOapg.properties.power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utilization"]) -> MetaOapg.properties.utilization: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "topology", "id", "panels", "idealOpenCircuitVoltage", "idealShortCircuitCurrent", "current", "voltage", "maxPower", "maxPowerVoltage", "maxPowerCurrent", "openCircuitVoltage", "power", "utilization", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["panels"]) -> typing.Union[MetaOapg.properties.panels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idealOpenCircuitVoltage"]) -> typing.Union[MetaOapg.properties.idealOpenCircuitVoltage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idealShortCircuitCurrent"]) -> typing.Union[MetaOapg.properties.idealShortCircuitCurrent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> typing.Union[MetaOapg.properties.current, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voltage"]) -> typing.Union[MetaOapg.properties.voltage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPower"]) -> typing.Union[MetaOapg.properties.maxPower, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPowerVoltage"]) -> typing.Union[MetaOapg.properties.maxPowerVoltage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPowerCurrent"]) -> typing.Union[MetaOapg.properties.maxPowerCurrent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["openCircuitVoltage"]) -> typing.Union[MetaOapg.properties.openCircuitVoltage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["power"]) -> typing.Union[MetaOapg.properties.power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utilization"]) -> typing.Union[MetaOapg.properties.utilization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "topology", "id", "panels", "idealOpenCircuitVoltage", "idealShortCircuitCurrent", "current", "voltage", "maxPower", "maxPowerVoltage", "maxPowerCurrent", "openCircuitVoltage", "power", "utilization", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        topology: typing.Union[MetaOapg.properties.topology, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        panels: typing.Union[MetaOapg.properties.panels, list, tuple, schemas.Unset] = schemas.unset,
        idealOpenCircuitVoltage: typing.Union[MetaOapg.properties.idealOpenCircuitVoltage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        idealShortCircuitCurrent: typing.Union[MetaOapg.properties.idealShortCircuitCurrent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        current: typing.Union[MetaOapg.properties.current, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        voltage: typing.Union[MetaOapg.properties.voltage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxPower: typing.Union[MetaOapg.properties.maxPower, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxPowerVoltage: typing.Union[MetaOapg.properties.maxPowerVoltage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxPowerCurrent: typing.Union[MetaOapg.properties.maxPowerCurrent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        openCircuitVoltage: typing.Union[MetaOapg.properties.openCircuitVoltage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        power: typing.Union[MetaOapg.properties.power, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        utilization: typing.Union[MetaOapg.properties.utilization, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SolarArray':
        return super().__new__(
            cls,
            *_args,
            topology=topology,
            name=name,
            id=id,
            panels=panels,
            idealOpenCircuitVoltage=idealOpenCircuitVoltage,
            idealShortCircuitCurrent=idealShortCircuitCurrent,
            current=current,
            voltage=voltage,
            maxPower=maxPower,
            maxPowerVoltage=maxPowerVoltage,
            maxPowerCurrent=maxPowerCurrent,
            openCircuitVoltage=openCircuitVoltage,
            power=power,
            utilization=utilization,
            _configuration=_configuration,
            **kwargs,
        )
