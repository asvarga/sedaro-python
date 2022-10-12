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


class TargetVector(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "vectorType",
            "name",
            "satellite",
            "targetPointingDirection",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            
            
            class vectorType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "TARGET": "TARGET",
                    }
                
                @schemas.classproperty
                def TARGET(cls):
                    return cls("TARGET")
            satellite = schemas.StrSchema
        
            @staticmethod
            def targetPointingDirection() -> typing.Type['TargetPointingDirections']:
                return TargetPointingDirections
            id = schemas.StrSchema
            
            
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
            
            
            class estimate(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'estimate':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class pointingModes_A(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pointingModes_A':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class pointingModes_B(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pointingModes_B':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class FOVConstraints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'FOVConstraints':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class directionSensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'directionSensors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class vectorSensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vectorSensors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            target = schemas.StrSchema
            targetGroup = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "vectorType": vectorType,
                "satellite": satellite,
                "targetPointingDirection": targetPointingDirection,
                "id": id,
                "truth": truth,
                "estimate": estimate,
                "pointingModes_A": pointingModes_A,
                "pointingModes_B": pointingModes_B,
                "FOVConstraints": FOVConstraints,
                "directionSensors": directionSensors,
                "vectorSensors": vectorSensors,
                "target": target,
                "targetGroup": targetGroup,
            }
    
    vectorType: MetaOapg.properties.vectorType
    name: MetaOapg.properties.name
    satellite: MetaOapg.properties.satellite
    targetPointingDirection: 'TargetPointingDirections'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vectorType"]) -> MetaOapg.properties.vectorType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetPointingDirection"]) -> 'TargetPointingDirections': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["truth"]) -> MetaOapg.properties.truth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimate"]) -> MetaOapg.properties.estimate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingModes_A"]) -> MetaOapg.properties.pointingModes_A: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingModes_B"]) -> MetaOapg.properties.pointingModes_B: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FOVConstraints"]) -> MetaOapg.properties.FOVConstraints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directionSensors"]) -> MetaOapg.properties.directionSensors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vectorSensors"]) -> MetaOapg.properties.vectorSensors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> MetaOapg.properties.target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroup"]) -> MetaOapg.properties.targetGroup: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "vectorType", "satellite", "targetPointingDirection", "id", "truth", "estimate", "pointingModes_A", "pointingModes_B", "FOVConstraints", "directionSensors", "vectorSensors", "target", "targetGroup", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vectorType"]) -> MetaOapg.properties.vectorType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetPointingDirection"]) -> 'TargetPointingDirections': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["truth"]) -> typing.Union[MetaOapg.properties.truth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimate"]) -> typing.Union[MetaOapg.properties.estimate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingModes_A"]) -> typing.Union[MetaOapg.properties.pointingModes_A, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingModes_B"]) -> typing.Union[MetaOapg.properties.pointingModes_B, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FOVConstraints"]) -> typing.Union[MetaOapg.properties.FOVConstraints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directionSensors"]) -> typing.Union[MetaOapg.properties.directionSensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vectorSensors"]) -> typing.Union[MetaOapg.properties.vectorSensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> typing.Union[MetaOapg.properties.target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroup"]) -> typing.Union[MetaOapg.properties.targetGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "vectorType", "satellite", "targetPointingDirection", "id", "truth", "estimate", "pointingModes_A", "pointingModes_B", "FOVConstraints", "directionSensors", "vectorSensors", "target", "targetGroup", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vectorType: typing.Union[MetaOapg.properties.vectorType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        satellite: typing.Union[MetaOapg.properties.satellite, str, ],
        targetPointingDirection: 'TargetPointingDirections',
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        truth: typing.Union[MetaOapg.properties.truth, list, tuple, schemas.Unset] = schemas.unset,
        estimate: typing.Union[MetaOapg.properties.estimate, list, tuple, schemas.Unset] = schemas.unset,
        pointingModes_A: typing.Union[MetaOapg.properties.pointingModes_A, list, tuple, schemas.Unset] = schemas.unset,
        pointingModes_B: typing.Union[MetaOapg.properties.pointingModes_B, list, tuple, schemas.Unset] = schemas.unset,
        FOVConstraints: typing.Union[MetaOapg.properties.FOVConstraints, list, tuple, schemas.Unset] = schemas.unset,
        directionSensors: typing.Union[MetaOapg.properties.directionSensors, list, tuple, schemas.Unset] = schemas.unset,
        vectorSensors: typing.Union[MetaOapg.properties.vectorSensors, list, tuple, schemas.Unset] = schemas.unset,
        target: typing.Union[MetaOapg.properties.target, str, schemas.Unset] = schemas.unset,
        targetGroup: typing.Union[MetaOapg.properties.targetGroup, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TargetVector':
        return super().__new__(
            cls,
            *args,
            vectorType=vectorType,
            name=name,
            satellite=satellite,
            targetPointingDirection=targetPointingDirection,
            id=id,
            truth=truth,
            estimate=estimate,
            pointingModes_A=pointingModes_A,
            pointingModes_B=pointingModes_B,
            FOVConstraints=FOVConstraints,
            directionSensors=directionSensors,
            vectorSensors=vectorSensors,
            target=target,
            targetGroup=targetGroup,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro.model.target_pointing_directions import TargetPointingDirections
