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


class GroupCondition(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "paramACategory",
            "paramBCategory",
            "name",
            "relationship",
            "paramA",
            "conOps",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            
            
            class relationship(
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
                            ConditionRelationship,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationship':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class paramACategory(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "TARGET_GROUP": "TARGET_GROUP",
                    }
                
                @schemas.classproperty
                def TARGET_GROUP(cls):
                    return cls("TARGET_GROUP")
            
            
            class paramBCategory(
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
                            ParameterBCategories,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'paramBCategory':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class paramA(
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
                            Parameters,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'paramA':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            conOps = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class paramB(
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
                            Parameters,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'paramB':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            scalar = schemas.NumberSchema
            targetA = schemas.StrSchema
            targetB = schemas.StrSchema
            targetGroupA = schemas.StrSchema
            
            
            class operationalModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'operationalModes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "relationship": relationship,
                "paramACategory": paramACategory,
                "paramBCategory": paramBCategory,
                "paramA": paramA,
                "conOps": conOps,
                "id": id,
                "paramB": paramB,
                "scalar": scalar,
                "targetA": targetA,
                "targetB": targetB,
                "targetGroupA": targetGroupA,
                "operationalModes": operationalModes,
            }
    
    paramACategory: MetaOapg.properties.paramACategory
    paramBCategory: MetaOapg.properties.paramBCategory
    name: MetaOapg.properties.name
    relationship: MetaOapg.properties.relationship
    paramA: MetaOapg.properties.paramA
    conOps: MetaOapg.properties.conOps
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationship"]) -> MetaOapg.properties.relationship: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paramACategory"]) -> MetaOapg.properties.paramACategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paramBCategory"]) -> MetaOapg.properties.paramBCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paramA"]) -> MetaOapg.properties.paramA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paramB"]) -> MetaOapg.properties.paramB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scalar"]) -> MetaOapg.properties.scalar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetA"]) -> MetaOapg.properties.targetA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetB"]) -> MetaOapg.properties.targetB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroupA"]) -> MetaOapg.properties.targetGroupA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationalModes"]) -> MetaOapg.properties.operationalModes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "relationship", "paramACategory", "paramBCategory", "paramA", "conOps", "id", "paramB", "scalar", "targetA", "targetB", "targetGroupA", "operationalModes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationship"]) -> MetaOapg.properties.relationship: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paramACategory"]) -> MetaOapg.properties.paramACategory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paramBCategory"]) -> MetaOapg.properties.paramBCategory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paramA"]) -> MetaOapg.properties.paramA: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paramB"]) -> typing.Union[MetaOapg.properties.paramB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scalar"]) -> typing.Union[MetaOapg.properties.scalar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetA"]) -> typing.Union[MetaOapg.properties.targetA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetB"]) -> typing.Union[MetaOapg.properties.targetB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroupA"]) -> typing.Union[MetaOapg.properties.targetGroupA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationalModes"]) -> typing.Union[MetaOapg.properties.operationalModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "relationship", "paramACategory", "paramBCategory", "paramA", "conOps", "id", "paramB", "scalar", "targetA", "targetB", "targetGroupA", "operationalModes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paramACategory: typing.Union[MetaOapg.properties.paramACategory, str, ],
        paramBCategory: typing.Union[MetaOapg.properties.paramBCategory, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        relationship: typing.Union[MetaOapg.properties.relationship, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        paramA: typing.Union[MetaOapg.properties.paramA, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        conOps: typing.Union[MetaOapg.properties.conOps, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        paramB: typing.Union[MetaOapg.properties.paramB, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        scalar: typing.Union[MetaOapg.properties.scalar, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        targetA: typing.Union[MetaOapg.properties.targetA, str, schemas.Unset] = schemas.unset,
        targetB: typing.Union[MetaOapg.properties.targetB, str, schemas.Unset] = schemas.unset,
        targetGroupA: typing.Union[MetaOapg.properties.targetGroupA, str, schemas.Unset] = schemas.unset,
        operationalModes: typing.Union[MetaOapg.properties.operationalModes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupCondition':
        return super().__new__(
            cls,
            *args,
            paramACategory=paramACategory,
            paramBCategory=paramBCategory,
            name=name,
            relationship=relationship,
            paramA=paramA,
            conOps=conOps,
            id=id,
            paramB=paramB,
            scalar=scalar,
            targetA=targetA,
            targetB=targetB,
            targetGroupA=targetGroupA,
            operationalModes=operationalModes,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.condition_relationship import ConditionRelationship
from sedaro_base_client.model.parameter_b_categories import ParameterBCategories
from sedaro_base_client.model.parameters import Parameters
