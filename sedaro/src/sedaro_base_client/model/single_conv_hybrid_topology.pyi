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


class SingleConvHybridTopology(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "componentType",
            "topologyType",
            "name",
            "subsystem",
            "battery",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            subsystem = schemas.StrSchema
            
            
            class componentType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def POWER_PROCESSOR(cls):
                    return cls("POWER_PROCESSOR")
            
            
            class topologyType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SINGLE_CONV_HYBRID(cls):
                    return cls("SINGLE_CONV_HYBRID")
            battery = schemas.StrSchema
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
            
            
            class cotsTemplate(
                schemas.StrSchema
            ):
                pass
            
            
            class loadStates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'loadStates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            satellite = schemas.StrSchema
            
            
            class thermal_interface_A(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thermal_interface_A':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class thermal_interface_B(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thermal_interface_B':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            powerConsumed = schemas.NumberSchema
            
            
            class dissipations(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.NumberSchema
                    ):
                        pass
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, decimal.Decimal, int, float, ],
                ) -> 'dissipations':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            hotMargin = schemas.NumberSchema
            coldMargin = schemas.NumberSchema
            
            
            class tempControllers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tempControllers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class temperature(
                schemas.NumberSchema
            ):
                pass
            
            
            class topologyParams(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            TopologyParamFRD,
                            TopologyParamSCH,
                            TopologyParamQRD,
                            TopologyParamTCM,
                            TopologyParamSCM,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'topologyParams':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class loads(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'loads':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class batteryCells(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'batteryCells':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class busRegulators(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'busRegulators':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class solarArrays(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'solarArrays':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class solarCells(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'solarCells':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            availableSolarRootPower = schemas.NumberSchema
            solarRootPower = schemas.NumberSchema
            __annotations__ = {
                "name": name,
                "subsystem": subsystem,
                "componentType": componentType,
                "topologyType": topologyType,
                "battery": battery,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
                "thermalCapacitance": thermalCapacitance,
                "cotsTemplate": cotsTemplate,
                "loadStates": loadStates,
                "satellite": satellite,
                "thermal_interface_A": thermal_interface_A,
                "thermal_interface_B": thermal_interface_B,
                "powerConsumed": powerConsumed,
                "dissipations": dissipations,
                "hotMargin": hotMargin,
                "coldMargin": coldMargin,
                "tempControllers": tempControllers,
                "temperature": temperature,
                "topologyParams": topologyParams,
                "loads": loads,
                "batteryCells": batteryCells,
                "busRegulators": busRegulators,
                "solarArrays": solarArrays,
                "solarCells": solarCells,
                "availableSolarRootPower": availableSolarRootPower,
                "solarRootPower": solarRootPower,
            }
    
    componentType: MetaOapg.properties.componentType
    topologyType: MetaOapg.properties.topologyType
    name: MetaOapg.properties.name
    subsystem: MetaOapg.properties.subsystem
    battery: MetaOapg.properties.battery
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subsystem"]) -> MetaOapg.properties.subsystem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentType"]) -> MetaOapg.properties.componentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topologyType"]) -> MetaOapg.properties.topologyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["battery"]) -> MetaOapg.properties.battery: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["cotsTemplate"]) -> MetaOapg.properties.cotsTemplate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadStates"]) -> MetaOapg.properties.loadStates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermal_interface_A"]) -> MetaOapg.properties.thermal_interface_A: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermal_interface_B"]) -> MetaOapg.properties.thermal_interface_B: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerConsumed"]) -> MetaOapg.properties.powerConsumed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dissipations"]) -> MetaOapg.properties.dissipations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotMargin"]) -> MetaOapg.properties.hotMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldMargin"]) -> MetaOapg.properties.coldMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tempControllers"]) -> MetaOapg.properties.tempControllers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topologyParams"]) -> MetaOapg.properties.topologyParams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loads"]) -> MetaOapg.properties.loads: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batteryCells"]) -> MetaOapg.properties.batteryCells: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["busRegulators"]) -> MetaOapg.properties.busRegulators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["solarArrays"]) -> MetaOapg.properties.solarArrays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["solarCells"]) -> MetaOapg.properties.solarCells: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableSolarRootPower"]) -> MetaOapg.properties.availableSolarRootPower: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["solarRootPower"]) -> MetaOapg.properties.solarRootPower: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "subsystem", "componentType", "topologyType", "battery", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "cotsTemplate", "loadStates", "satellite", "thermal_interface_A", "thermal_interface_B", "powerConsumed", "dissipations", "hotMargin", "coldMargin", "tempControllers", "temperature", "topologyParams", "loads", "batteryCells", "busRegulators", "solarArrays", "solarCells", "availableSolarRootPower", "solarRootPower", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subsystem"]) -> MetaOapg.properties.subsystem: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentType"]) -> MetaOapg.properties.componentType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topologyType"]) -> MetaOapg.properties.topologyType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["battery"]) -> MetaOapg.properties.battery: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["cotsTemplate"]) -> typing.Union[MetaOapg.properties.cotsTemplate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadStates"]) -> typing.Union[MetaOapg.properties.loadStates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> typing.Union[MetaOapg.properties.satellite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermal_interface_A"]) -> typing.Union[MetaOapg.properties.thermal_interface_A, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermal_interface_B"]) -> typing.Union[MetaOapg.properties.thermal_interface_B, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerConsumed"]) -> typing.Union[MetaOapg.properties.powerConsumed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dissipations"]) -> typing.Union[MetaOapg.properties.dissipations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotMargin"]) -> typing.Union[MetaOapg.properties.hotMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldMargin"]) -> typing.Union[MetaOapg.properties.coldMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tempControllers"]) -> typing.Union[MetaOapg.properties.tempControllers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> typing.Union[MetaOapg.properties.temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topologyParams"]) -> typing.Union[MetaOapg.properties.topologyParams, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loads"]) -> typing.Union[MetaOapg.properties.loads, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batteryCells"]) -> typing.Union[MetaOapg.properties.batteryCells, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["busRegulators"]) -> typing.Union[MetaOapg.properties.busRegulators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["solarArrays"]) -> typing.Union[MetaOapg.properties.solarArrays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["solarCells"]) -> typing.Union[MetaOapg.properties.solarCells, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableSolarRootPower"]) -> typing.Union[MetaOapg.properties.availableSolarRootPower, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["solarRootPower"]) -> typing.Union[MetaOapg.properties.solarRootPower, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "subsystem", "componentType", "topologyType", "battery", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "cotsTemplate", "loadStates", "satellite", "thermal_interface_A", "thermal_interface_B", "powerConsumed", "dissipations", "hotMargin", "coldMargin", "tempControllers", "temperature", "topologyParams", "loads", "batteryCells", "busRegulators", "solarArrays", "solarCells", "availableSolarRootPower", "solarRootPower", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        componentType: typing.Union[MetaOapg.properties.componentType, str, ],
        topologyType: typing.Union[MetaOapg.properties.topologyType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        subsystem: typing.Union[MetaOapg.properties.subsystem, str, ],
        battery: typing.Union[MetaOapg.properties.battery, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        thermalCapacitance: typing.Union[MetaOapg.properties.thermalCapacitance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        cotsTemplate: typing.Union[MetaOapg.properties.cotsTemplate, str, schemas.Unset] = schemas.unset,
        loadStates: typing.Union[MetaOapg.properties.loadStates, list, tuple, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        thermal_interface_A: typing.Union[MetaOapg.properties.thermal_interface_A, list, tuple, schemas.Unset] = schemas.unset,
        thermal_interface_B: typing.Union[MetaOapg.properties.thermal_interface_B, list, tuple, schemas.Unset] = schemas.unset,
        powerConsumed: typing.Union[MetaOapg.properties.powerConsumed, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dissipations: typing.Union[MetaOapg.properties.dissipations, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        hotMargin: typing.Union[MetaOapg.properties.hotMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldMargin: typing.Union[MetaOapg.properties.coldMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tempControllers: typing.Union[MetaOapg.properties.tempControllers, list, tuple, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        topologyParams: typing.Union[MetaOapg.properties.topologyParams, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        loads: typing.Union[MetaOapg.properties.loads, list, tuple, schemas.Unset] = schemas.unset,
        batteryCells: typing.Union[MetaOapg.properties.batteryCells, list, tuple, schemas.Unset] = schemas.unset,
        busRegulators: typing.Union[MetaOapg.properties.busRegulators, list, tuple, schemas.Unset] = schemas.unset,
        solarArrays: typing.Union[MetaOapg.properties.solarArrays, list, tuple, schemas.Unset] = schemas.unset,
        solarCells: typing.Union[MetaOapg.properties.solarCells, list, tuple, schemas.Unset] = schemas.unset,
        availableSolarRootPower: typing.Union[MetaOapg.properties.availableSolarRootPower, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        solarRootPower: typing.Union[MetaOapg.properties.solarRootPower, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SingleConvHybridTopology':
        return super().__new__(
            cls,
            *args,
            componentType=componentType,
            topologyType=topologyType,
            name=name,
            subsystem=subsystem,
            battery=battery,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            hotTempRating=hotTempRating,
            coldTempRating=coldTempRating,
            thermalCapacitance=thermalCapacitance,
            cotsTemplate=cotsTemplate,
            loadStates=loadStates,
            satellite=satellite,
            thermal_interface_A=thermal_interface_A,
            thermal_interface_B=thermal_interface_B,
            powerConsumed=powerConsumed,
            dissipations=dissipations,
            hotMargin=hotMargin,
            coldMargin=coldMargin,
            tempControllers=tempControllers,
            temperature=temperature,
            topologyParams=topologyParams,
            loads=loads,
            batteryCells=batteryCells,
            busRegulators=busRegulators,
            solarArrays=solarArrays,
            solarCells=solarCells,
            availableSolarRootPower=availableSolarRootPower,
            solarRootPower=solarRootPower,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.topology_param_frd import TopologyParamFRD
from sedaro_base_client.model.topology_param_qrd import TopologyParamQRD
from sedaro_base_client.model.topology_param_sch import TopologyParamSCH
from sedaro_base_client.model.topology_param_scm import TopologyParamSCM
from sedaro_base_client.model.topology_param_tcm import TopologyParamTCM
