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


class VectorSensor(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "componentType",
            "name",
            "oneSigmaPerAxisError",
            "subsystem",
            "referenceVector",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            subsystem = schemas.StrSchema
            
            
            class componentType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "VECTOR_SENSOR": "VECTOR_SENSOR",
                    }
                
                @schemas.classproperty
                def VECTOR_SENSOR(cls):
                    return cls("VECTOR_SENSOR")
            oneSigmaPerAxisError = schemas.NumberSchema
            referenceVector = schemas.StrSchema
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
            hotTempRating = schemas.NumberSchema
            coldTempRating = schemas.NumberSchema
            
            
            class thermalCapacitance(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            temperature = schemas.NumberSchema
            
            
            class cotsTemplate(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            
            
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
            
            
            class dissipations(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.NumberSchema
                    ):
                    
                    
                        class MetaOapg:
                            inclusive_minimum = 0.0
                
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
            fieldOfView = schemas.StrSchema
            
            
            class truth(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'truth':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class measurement(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'measurement':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class triadAlgorithms(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'triadAlgorithms':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "subsystem": subsystem,
                "componentType": componentType,
                "oneSigmaPerAxisError": oneSigmaPerAxisError,
                "referenceVector": referenceVector,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
                "thermalCapacitance": thermalCapacitance,
                "temperature": temperature,
                "cotsTemplate": cotsTemplate,
                "loadStates": loadStates,
                "satellite": satellite,
                "thermal_interface_A": thermal_interface_A,
                "thermal_interface_B": thermal_interface_B,
                "dissipations": dissipations,
                "hotMargin": hotMargin,
                "coldMargin": coldMargin,
                "tempControllers": tempControllers,
                "fieldOfView": fieldOfView,
                "truth": truth,
                "measurement": measurement,
                "triadAlgorithms": triadAlgorithms,
            }
    
    componentType: MetaOapg.properties.componentType
    name: MetaOapg.properties.name
    oneSigmaPerAxisError: MetaOapg.properties.oneSigmaPerAxisError
    subsystem: MetaOapg.properties.subsystem
    referenceVector: MetaOapg.properties.referenceVector
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subsystem"]) -> MetaOapg.properties.subsystem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentType"]) -> MetaOapg.properties.componentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oneSigmaPerAxisError"]) -> MetaOapg.properties.oneSigmaPerAxisError: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceVector"]) -> MetaOapg.properties.referenceVector: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["dissipations"]) -> MetaOapg.properties.dissipations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotMargin"]) -> MetaOapg.properties.hotMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldMargin"]) -> MetaOapg.properties.coldMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tempControllers"]) -> MetaOapg.properties.tempControllers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldOfView"]) -> MetaOapg.properties.fieldOfView: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["truth"]) -> MetaOapg.properties.truth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["measurement"]) -> MetaOapg.properties.measurement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triadAlgorithms"]) -> MetaOapg.properties.triadAlgorithms: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "subsystem", "componentType", "oneSigmaPerAxisError", "referenceVector", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "temperature", "cotsTemplate", "loadStates", "satellite", "thermal_interface_A", "thermal_interface_B", "dissipations", "hotMargin", "coldMargin", "tempControllers", "fieldOfView", "truth", "measurement", "triadAlgorithms", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subsystem"]) -> MetaOapg.properties.subsystem: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentType"]) -> MetaOapg.properties.componentType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oneSigmaPerAxisError"]) -> MetaOapg.properties.oneSigmaPerAxisError: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceVector"]) -> MetaOapg.properties.referenceVector: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["dissipations"]) -> typing.Union[MetaOapg.properties.dissipations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotMargin"]) -> typing.Union[MetaOapg.properties.hotMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldMargin"]) -> typing.Union[MetaOapg.properties.coldMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tempControllers"]) -> typing.Union[MetaOapg.properties.tempControllers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldOfView"]) -> typing.Union[MetaOapg.properties.fieldOfView, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["truth"]) -> typing.Union[MetaOapg.properties.truth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["measurement"]) -> typing.Union[MetaOapg.properties.measurement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triadAlgorithms"]) -> typing.Union[MetaOapg.properties.triadAlgorithms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "subsystem", "componentType", "oneSigmaPerAxisError", "referenceVector", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "temperature", "cotsTemplate", "loadStates", "satellite", "thermal_interface_A", "thermal_interface_B", "dissipations", "hotMargin", "coldMargin", "tempControllers", "fieldOfView", "truth", "measurement", "triadAlgorithms", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        componentType: typing.Union[MetaOapg.properties.componentType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        oneSigmaPerAxisError: typing.Union[MetaOapg.properties.oneSigmaPerAxisError, decimal.Decimal, int, float, ],
        subsystem: typing.Union[MetaOapg.properties.subsystem, str, ],
        referenceVector: typing.Union[MetaOapg.properties.referenceVector, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        thermalCapacitance: typing.Union[MetaOapg.properties.thermalCapacitance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        cotsTemplate: typing.Union[MetaOapg.properties.cotsTemplate, str, schemas.Unset] = schemas.unset,
        loadStates: typing.Union[MetaOapg.properties.loadStates, list, tuple, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        thermal_interface_A: typing.Union[MetaOapg.properties.thermal_interface_A, list, tuple, schemas.Unset] = schemas.unset,
        thermal_interface_B: typing.Union[MetaOapg.properties.thermal_interface_B, list, tuple, schemas.Unset] = schemas.unset,
        dissipations: typing.Union[MetaOapg.properties.dissipations, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        hotMargin: typing.Union[MetaOapg.properties.hotMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldMargin: typing.Union[MetaOapg.properties.coldMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tempControllers: typing.Union[MetaOapg.properties.tempControllers, list, tuple, schemas.Unset] = schemas.unset,
        fieldOfView: typing.Union[MetaOapg.properties.fieldOfView, str, schemas.Unset] = schemas.unset,
        truth: typing.Union[MetaOapg.properties.truth, list, tuple, schemas.Unset] = schemas.unset,
        measurement: typing.Union[MetaOapg.properties.measurement, list, tuple, schemas.Unset] = schemas.unset,
        triadAlgorithms: typing.Union[MetaOapg.properties.triadAlgorithms, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VectorSensor':
        return super().__new__(
            cls,
            *args,
            componentType=componentType,
            name=name,
            oneSigmaPerAxisError=oneSigmaPerAxisError,
            subsystem=subsystem,
            referenceVector=referenceVector,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            hotTempRating=hotTempRating,
            coldTempRating=coldTempRating,
            thermalCapacitance=thermalCapacitance,
            temperature=temperature,
            cotsTemplate=cotsTemplate,
            loadStates=loadStates,
            satellite=satellite,
            thermal_interface_A=thermal_interface_A,
            thermal_interface_B=thermal_interface_B,
            dissipations=dissipations,
            hotMargin=hotMargin,
            coldMargin=coldMargin,
            tempControllers=tempControllers,
            fieldOfView=fieldOfView,
            truth=truth,
            measurement=measurement,
            triadAlgorithms=triadAlgorithms,
            _configuration=_configuration,
            **kwargs,
        )
