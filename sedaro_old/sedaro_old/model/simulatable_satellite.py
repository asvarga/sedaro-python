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


class SimulatableSatellite(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "cadScaleFactor",
            "cadSignedUrl",
            "topology",
            "cadKey",
        }
        
        class properties:
            
            
            class cadKey(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 48
            
            
            class cadSignedUrl(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 1024
            cadScaleFactor = schemas.NumberSchema
            topology = schemas.StrSchema
            id = schemas.StrSchema
            mass = schemas.NumberSchema
            inertia = schemas.AnyTypeSchema
            earthshineIrradiance = schemas.NumberSchema
            
            
            class albedo(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            
            
            class dragTorque(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dragTorque':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class gravityGradientTorque(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gravityGradientTorque':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class cadFileName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class bodyFrameVectors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bodyFrameVectors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
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
            
            
            class subsystems(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subsystems':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class referenceVectors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'referenceVectors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class components(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'components':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class interfaces(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'interfaces':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class coolers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'coolers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class heaters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'heaters':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class reactionWheels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'reactionWheels':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class magnetorquers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'magnetorquers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class algorithms(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'algorithms':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class DEFAULT_CAD_MODELS(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'DEFAULT_CAD_MODELS':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class commandedAltitude(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'commandedAltitude':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class commandedAngularRates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'commandedAngularRates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "cadKey": cadKey,
                "cadSignedUrl": cadSignedUrl,
                "cadScaleFactor": cadScaleFactor,
                "topology": topology,
                "id": id,
                "mass": mass,
                "inertia": inertia,
                "earthshineIrradiance": earthshineIrradiance,
                "albedo": albedo,
                "dragTorque": dragTorque,
                "gravityGradientTorque": gravityGradientTorque,
                "cadFileName": cadFileName,
                "bodyFrameVectors": bodyFrameVectors,
                "surfaces": surfaces,
                "solarArrays": solarArrays,
                "subsystems": subsystems,
                "referenceVectors": referenceVectors,
                "components": components,
                "interfaces": interfaces,
                "coolers": coolers,
                "heaters": heaters,
                "reactionWheels": reactionWheels,
                "magnetorquers": magnetorquers,
                "algorithms": algorithms,
                "DEFAULT_CAD_MODELS": DEFAULT_CAD_MODELS,
                "commandedAltitude": commandedAltitude,
                "commandedAngularRates": commandedAngularRates,
            }
    
    cadScaleFactor: MetaOapg.properties.cadScaleFactor
    cadSignedUrl: MetaOapg.properties.cadSignedUrl
    topology: MetaOapg.properties.topology
    cadKey: MetaOapg.properties.cadKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadKey"]) -> MetaOapg.properties.cadKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadSignedUrl"]) -> MetaOapg.properties.cadSignedUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadScaleFactor"]) -> MetaOapg.properties.cadScaleFactor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mass"]) -> MetaOapg.properties.mass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inertia"]) -> MetaOapg.properties.inertia: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earthshineIrradiance"]) -> MetaOapg.properties.earthshineIrradiance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["albedo"]) -> MetaOapg.properties.albedo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dragTorque"]) -> MetaOapg.properties.dragTorque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gravityGradientTorque"]) -> MetaOapg.properties.gravityGradientTorque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadFileName"]) -> MetaOapg.properties.cadFileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyFrameVectors"]) -> MetaOapg.properties.bodyFrameVectors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaces"]) -> MetaOapg.properties.surfaces: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["solarArrays"]) -> MetaOapg.properties.solarArrays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subsystems"]) -> MetaOapg.properties.subsystems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceVectors"]) -> MetaOapg.properties.referenceVectors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["components"]) -> MetaOapg.properties.components: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interfaces"]) -> MetaOapg.properties.interfaces: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coolers"]) -> MetaOapg.properties.coolers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heaters"]) -> MetaOapg.properties.heaters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactionWheels"]) -> MetaOapg.properties.reactionWheels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["magnetorquers"]) -> MetaOapg.properties.magnetorquers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithms"]) -> MetaOapg.properties.algorithms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DEFAULT_CAD_MODELS"]) -> MetaOapg.properties.DEFAULT_CAD_MODELS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedAltitude"]) -> MetaOapg.properties.commandedAltitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedAngularRates"]) -> MetaOapg.properties.commandedAngularRates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cadKey", "cadSignedUrl", "cadScaleFactor", "topology", "id", "mass", "inertia", "earthshineIrradiance", "albedo", "dragTorque", "gravityGradientTorque", "cadFileName", "bodyFrameVectors", "surfaces", "solarArrays", "subsystems", "referenceVectors", "components", "interfaces", "coolers", "heaters", "reactionWheels", "magnetorquers", "algorithms", "DEFAULT_CAD_MODELS", "commandedAltitude", "commandedAngularRates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadKey"]) -> MetaOapg.properties.cadKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadSignedUrl"]) -> MetaOapg.properties.cadSignedUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadScaleFactor"]) -> MetaOapg.properties.cadScaleFactor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mass"]) -> typing.Union[MetaOapg.properties.mass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inertia"]) -> typing.Union[MetaOapg.properties.inertia, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earthshineIrradiance"]) -> typing.Union[MetaOapg.properties.earthshineIrradiance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["albedo"]) -> typing.Union[MetaOapg.properties.albedo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dragTorque"]) -> typing.Union[MetaOapg.properties.dragTorque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gravityGradientTorque"]) -> typing.Union[MetaOapg.properties.gravityGradientTorque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadFileName"]) -> typing.Union[MetaOapg.properties.cadFileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyFrameVectors"]) -> typing.Union[MetaOapg.properties.bodyFrameVectors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaces"]) -> typing.Union[MetaOapg.properties.surfaces, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["solarArrays"]) -> typing.Union[MetaOapg.properties.solarArrays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subsystems"]) -> typing.Union[MetaOapg.properties.subsystems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceVectors"]) -> typing.Union[MetaOapg.properties.referenceVectors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["components"]) -> typing.Union[MetaOapg.properties.components, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interfaces"]) -> typing.Union[MetaOapg.properties.interfaces, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coolers"]) -> typing.Union[MetaOapg.properties.coolers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heaters"]) -> typing.Union[MetaOapg.properties.heaters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactionWheels"]) -> typing.Union[MetaOapg.properties.reactionWheels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["magnetorquers"]) -> typing.Union[MetaOapg.properties.magnetorquers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithms"]) -> typing.Union[MetaOapg.properties.algorithms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DEFAULT_CAD_MODELS"]) -> typing.Union[MetaOapg.properties.DEFAULT_CAD_MODELS, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedAltitude"]) -> typing.Union[MetaOapg.properties.commandedAltitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedAngularRates"]) -> typing.Union[MetaOapg.properties.commandedAngularRates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cadKey", "cadSignedUrl", "cadScaleFactor", "topology", "id", "mass", "inertia", "earthshineIrradiance", "albedo", "dragTorque", "gravityGradientTorque", "cadFileName", "bodyFrameVectors", "surfaces", "solarArrays", "subsystems", "referenceVectors", "components", "interfaces", "coolers", "heaters", "reactionWheels", "magnetorquers", "algorithms", "DEFAULT_CAD_MODELS", "commandedAltitude", "commandedAngularRates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cadScaleFactor: typing.Union[MetaOapg.properties.cadScaleFactor, decimal.Decimal, int, float, ],
        cadSignedUrl: typing.Union[MetaOapg.properties.cadSignedUrl, str, ],
        topology: typing.Union[MetaOapg.properties.topology, str, ],
        cadKey: typing.Union[MetaOapg.properties.cadKey, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        mass: typing.Union[MetaOapg.properties.mass, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        inertia: typing.Union[MetaOapg.properties.inertia, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        earthshineIrradiance: typing.Union[MetaOapg.properties.earthshineIrradiance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        albedo: typing.Union[MetaOapg.properties.albedo, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dragTorque: typing.Union[MetaOapg.properties.dragTorque, list, tuple, schemas.Unset] = schemas.unset,
        gravityGradientTorque: typing.Union[MetaOapg.properties.gravityGradientTorque, list, tuple, schemas.Unset] = schemas.unset,
        cadFileName: typing.Union[MetaOapg.properties.cadFileName, str, schemas.Unset] = schemas.unset,
        bodyFrameVectors: typing.Union[MetaOapg.properties.bodyFrameVectors, list, tuple, schemas.Unset] = schemas.unset,
        surfaces: typing.Union[MetaOapg.properties.surfaces, list, tuple, schemas.Unset] = schemas.unset,
        solarArrays: typing.Union[MetaOapg.properties.solarArrays, list, tuple, schemas.Unset] = schemas.unset,
        subsystems: typing.Union[MetaOapg.properties.subsystems, list, tuple, schemas.Unset] = schemas.unset,
        referenceVectors: typing.Union[MetaOapg.properties.referenceVectors, list, tuple, schemas.Unset] = schemas.unset,
        components: typing.Union[MetaOapg.properties.components, list, tuple, schemas.Unset] = schemas.unset,
        interfaces: typing.Union[MetaOapg.properties.interfaces, list, tuple, schemas.Unset] = schemas.unset,
        coolers: typing.Union[MetaOapg.properties.coolers, list, tuple, schemas.Unset] = schemas.unset,
        heaters: typing.Union[MetaOapg.properties.heaters, list, tuple, schemas.Unset] = schemas.unset,
        reactionWheels: typing.Union[MetaOapg.properties.reactionWheels, list, tuple, schemas.Unset] = schemas.unset,
        magnetorquers: typing.Union[MetaOapg.properties.magnetorquers, list, tuple, schemas.Unset] = schemas.unset,
        algorithms: typing.Union[MetaOapg.properties.algorithms, list, tuple, schemas.Unset] = schemas.unset,
        DEFAULT_CAD_MODELS: typing.Union[MetaOapg.properties.DEFAULT_CAD_MODELS, list, tuple, schemas.Unset] = schemas.unset,
        commandedAltitude: typing.Union[MetaOapg.properties.commandedAltitude, list, tuple, schemas.Unset] = schemas.unset,
        commandedAngularRates: typing.Union[MetaOapg.properties.commandedAngularRates, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SimulatableSatellite':
        return super().__new__(
            cls,
            *args,
            cadScaleFactor=cadScaleFactor,
            cadSignedUrl=cadSignedUrl,
            topology=topology,
            cadKey=cadKey,
            id=id,
            mass=mass,
            inertia=inertia,
            earthshineIrradiance=earthshineIrradiance,
            albedo=albedo,
            dragTorque=dragTorque,
            gravityGradientTorque=gravityGradientTorque,
            cadFileName=cadFileName,
            bodyFrameVectors=bodyFrameVectors,
            surfaces=surfaces,
            solarArrays=solarArrays,
            subsystems=subsystems,
            referenceVectors=referenceVectors,
            components=components,
            interfaces=interfaces,
            coolers=coolers,
            heaters=heaters,
            reactionWheels=reactionWheels,
            magnetorquers=magnetorquers,
            algorithms=algorithms,
            DEFAULT_CAD_MODELS=DEFAULT_CAD_MODELS,
            commandedAltitude=commandedAltitude,
            commandedAngularRates=commandedAngularRates,
            _configuration=_configuration,
            **kwargs,
        )
