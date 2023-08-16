# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.5.2
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


class PolynomialEphemerisBody(
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
            "SUN": "SUN",
            "MOON": "MOON",
            "EARTH": "EARTH",
            "MERCURY": "MERCURY",
            "VENUS": "VENUS",
            "MARS": "MARS",
            "JUPITER": "JUPITER",
            "SATURN": "SATURN",
            "URANUS": "URANUS",
            "NEPTUNE": "NEPTUNE",
            "PLUTO": "PLUTO",
        }
    
    @schemas.classproperty
    def SUN(cls):
        return cls("SUN")
    
    @schemas.classproperty
    def MOON(cls):
        return cls("MOON")
    
    @schemas.classproperty
    def EARTH(cls):
        return cls("EARTH")
    
    @schemas.classproperty
    def MERCURY(cls):
        return cls("MERCURY")
    
    @schemas.classproperty
    def VENUS(cls):
        return cls("VENUS")
    
    @schemas.classproperty
    def MARS(cls):
        return cls("MARS")
    
    @schemas.classproperty
    def JUPITER(cls):
        return cls("JUPITER")
    
    @schemas.classproperty
    def SATURN(cls):
        return cls("SATURN")
    
    @schemas.classproperty
    def URANUS(cls):
        return cls("URANUS")
    
    @schemas.classproperty
    def NEPTUNE(cls):
        return cls("NEPTUNE")
    
    @schemas.classproperty
    def PLUTO(cls):
        return cls("PLUTO")
