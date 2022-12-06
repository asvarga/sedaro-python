# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.2.12
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


class SurfaceCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "area",
            "bodyFrameVector",
            "surfaceCentroid",
            "motionType",
            "name",
            "surfaceMaterial",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class motionType(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            MotionTypes,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'motionType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            area = schemas.NumberSchema
            
            
            class surfaceCentroid(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'surfaceCentroid':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            bodyFrameVector = schemas.StrSchema
            surfaceMaterial = schemas.StrSchema
            id = schemas.StrSchema
            satellite = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "motionType": motionType,
                "area": area,
                "surfaceCentroid": surfaceCentroid,
                "bodyFrameVector": bodyFrameVector,
                "surfaceMaterial": surfaceMaterial,
                "id": id,
                "satellite": satellite,
            }
    
    area: MetaOapg.properties.area
    bodyFrameVector: MetaOapg.properties.bodyFrameVector
    surfaceCentroid: MetaOapg.properties.surfaceCentroid
    motionType: MetaOapg.properties.motionType
    name: MetaOapg.properties.name
    surfaceMaterial: MetaOapg.properties.surfaceMaterial
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["motionType"]) -> MetaOapg.properties.motionType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceCentroid"]) -> MetaOapg.properties.surfaceCentroid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceMaterial"]) -> MetaOapg.properties.surfaceMaterial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "motionType", "area", "surfaceCentroid", "bodyFrameVector", "surfaceMaterial", "id", "satellite", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["motionType"]) -> MetaOapg.properties.motionType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceCentroid"]) -> MetaOapg.properties.surfaceCentroid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceMaterial"]) -> MetaOapg.properties.surfaceMaterial: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> typing.Union[MetaOapg.properties.satellite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "motionType", "area", "surfaceCentroid", "bodyFrameVector", "surfaceMaterial", "id", "satellite", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        area: typing.Union[MetaOapg.properties.area, decimal.Decimal, int, float, ],
        bodyFrameVector: typing.Union[MetaOapg.properties.bodyFrameVector, str, ],
        surfaceCentroid: typing.Union[MetaOapg.properties.surfaceCentroid, list, tuple, ],
        motionType: typing.Union[MetaOapg.properties.motionType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        surfaceMaterial: typing.Union[MetaOapg.properties.surfaceMaterial, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SurfaceCreate':
        return super().__new__(
            cls,
            *_args,
            area=area,
            bodyFrameVector=bodyFrameVector,
            surfaceCentroid=surfaceCentroid,
            motionType=motionType,
            name=name,
            surfaceMaterial=surfaceMaterial,
            id=id,
            satellite=satellite,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.motion_types import MotionTypes
