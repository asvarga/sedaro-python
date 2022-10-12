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


class RectangularFieldOfView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "widthHalfAngle",
            "boresightBodyFrameVector",
            "name",
            "heightBodyFrameVector",
            "heightHalfAngle",
            "fieldOfViewType",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            
            
            class fieldOfViewType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "RECT_FIELD_OF_VIEW": "RECT_FIELD_OF_VIEW",
                    }
                
                @schemas.classproperty
                def RECT_FIELD_OF_VIEW(cls):
                    return cls("RECT_FIELD_OF_VIEW")
            boresightBodyFrameVector = schemas.StrSchema
            
            
            class heightHalfAngle(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 180.0
                    inclusive_minimum = 0.0
            
            
            class widthHalfAngle(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 180.0
                    inclusive_minimum = 0.0
            heightBodyFrameVector = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class sensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sensors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class constraints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'constraints':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "fieldOfViewType": fieldOfViewType,
                "boresightBodyFrameVector": boresightBodyFrameVector,
                "heightHalfAngle": heightHalfAngle,
                "widthHalfAngle": widthHalfAngle,
                "heightBodyFrameVector": heightBodyFrameVector,
                "id": id,
                "sensors": sensors,
                "constraints": constraints,
            }
    
    widthHalfAngle: MetaOapg.properties.widthHalfAngle
    boresightBodyFrameVector: MetaOapg.properties.boresightBodyFrameVector
    name: MetaOapg.properties.name
    heightBodyFrameVector: MetaOapg.properties.heightBodyFrameVector
    heightHalfAngle: MetaOapg.properties.heightHalfAngle
    fieldOfViewType: MetaOapg.properties.fieldOfViewType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldOfViewType"]) -> MetaOapg.properties.fieldOfViewType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boresightBodyFrameVector"]) -> MetaOapg.properties.boresightBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heightHalfAngle"]) -> MetaOapg.properties.heightHalfAngle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["widthHalfAngle"]) -> MetaOapg.properties.widthHalfAngle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heightBodyFrameVector"]) -> MetaOapg.properties.heightBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensors"]) -> MetaOapg.properties.sensors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["constraints"]) -> MetaOapg.properties.constraints: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "fieldOfViewType", "boresightBodyFrameVector", "heightHalfAngle", "widthHalfAngle", "heightBodyFrameVector", "id", "sensors", "constraints", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldOfViewType"]) -> MetaOapg.properties.fieldOfViewType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["boresightBodyFrameVector"]) -> MetaOapg.properties.boresightBodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heightHalfAngle"]) -> MetaOapg.properties.heightHalfAngle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["widthHalfAngle"]) -> MetaOapg.properties.widthHalfAngle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heightBodyFrameVector"]) -> MetaOapg.properties.heightBodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensors"]) -> typing.Union[MetaOapg.properties.sensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["constraints"]) -> typing.Union[MetaOapg.properties.constraints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "fieldOfViewType", "boresightBodyFrameVector", "heightHalfAngle", "widthHalfAngle", "heightBodyFrameVector", "id", "sensors", "constraints", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        widthHalfAngle: typing.Union[MetaOapg.properties.widthHalfAngle, decimal.Decimal, int, float, ],
        boresightBodyFrameVector: typing.Union[MetaOapg.properties.boresightBodyFrameVector, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        heightBodyFrameVector: typing.Union[MetaOapg.properties.heightBodyFrameVector, str, ],
        heightHalfAngle: typing.Union[MetaOapg.properties.heightHalfAngle, decimal.Decimal, int, float, ],
        fieldOfViewType: typing.Union[MetaOapg.properties.fieldOfViewType, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        sensors: typing.Union[MetaOapg.properties.sensors, list, tuple, schemas.Unset] = schemas.unset,
        constraints: typing.Union[MetaOapg.properties.constraints, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RectangularFieldOfView':
        return super().__new__(
            cls,
            *args,
            widthHalfAngle=widthHalfAngle,
            boresightBodyFrameVector=boresightBodyFrameVector,
            name=name,
            heightBodyFrameVector=heightBodyFrameVector,
            heightHalfAngle=heightHalfAngle,
            fieldOfViewType=fieldOfViewType,
            id=id,
            sensors=sensors,
            constraints=constraints,
            _configuration=_configuration,
            **kwargs,
        )
