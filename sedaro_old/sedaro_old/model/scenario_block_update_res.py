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


class ScenarioBlockUpdateRes(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "action",
            "block",
            "branch",
        }
        
        class properties:
        
            @staticmethod
            def block() -> typing.Type['GroupAndId']:
                return GroupAndId
        
            @staticmethod
            def branch() -> typing.Type['PostgresBranchScenario']:
                return PostgresBranchScenario
            
            
            class action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "UPDATE": "UPDATE",
                    }
                
                @schemas.classproperty
                def UPDATE(cls):
                    return cls("UPDATE")
            __annotations__ = {
                "block": block,
                "branch": branch,
                "action": action,
            }
    
    action: MetaOapg.properties.action
    block: 'GroupAndId'
    branch: 'PostgresBranchScenario'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block"]) -> 'GroupAndId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branch"]) -> 'PostgresBranchScenario': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["block", "branch", "action", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block"]) -> 'GroupAndId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branch"]) -> 'PostgresBranchScenario': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["block", "branch", "action", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        action: typing.Union[MetaOapg.properties.action, str, ],
        block: 'GroupAndId',
        branch: 'PostgresBranchScenario',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScenarioBlockUpdateRes':
        return super().__new__(
            cls,
            *args,
            action=action,
            block=block,
            branch=branch,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_old.model.group_and_id import GroupAndId
from sedaro_old.model.postgres_branch_scenario import PostgresBranchScenario
