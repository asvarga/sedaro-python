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


class TopologyParamSCM(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "bcrEfficiency",
            "outputPowerRating",
        }
        
        class properties:
            
            
            class bcrEfficiency(
                schemas.NumberSchema
            ):
                pass
            
            
            class outputPowerRating(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "bcrEfficiency": bcrEfficiency,
                "outputPowerRating": outputPowerRating,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    bcrEfficiency: MetaOapg.properties.bcrEfficiency
    outputPowerRating: MetaOapg.properties.outputPowerRating
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["outputPowerRating"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["outputPowerRating"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bcrEfficiency: typing.Union[MetaOapg.properties.bcrEfficiency, decimal.Decimal, int, float, ],
        outputPowerRating: typing.Union[MetaOapg.properties.outputPowerRating, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TopologyParamSCM':
        return super().__new__(
            cls,
            *args,
            bcrEfficiency=bcrEfficiency,
            outputPowerRating=outputPowerRating,
            _configuration=_configuration,
        )
