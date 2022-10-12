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


class ConditionRelationship(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """


    class MetaOapg:
        enum_value_to_name = {
            "GREATER": "GREATER",
            "LESS": "LESS",
            "GREATER_EQUAL": "GREATER_EQUAL",
            "LESS_EQUAL": "LESS_EQUAL",
            "EQUAL": "EQUAL",
            "NOT_EQUAL": "NOT_EQUAL",
        }
    
    @schemas.classproperty
    def GREATER(cls):
        return cls("GREATER")
    
    @schemas.classproperty
    def LESS(cls):
        return cls("LESS")
    
    @schemas.classproperty
    def GREATER_EQUAL(cls):
        return cls("GREATER_EQUAL")
    
    @schemas.classproperty
    def LESS_EQUAL(cls):
        return cls("LESS_EQUAL")
    
    @schemas.classproperty
    def EQUAL(cls):
        return cls("EQUAL")
    
    @schemas.classproperty
    def NOT_EQUAL(cls):
        return cls("NOT_EQUAL")
