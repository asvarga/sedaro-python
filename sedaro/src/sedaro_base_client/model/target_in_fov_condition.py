# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.7
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


class TargetInFovCondition(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            id = schemas.StrSchema
        
            @staticmethod
            def metamodel() -> typing.Type['Metamodel']:
                return Metamodel
            terminator = schemas.BoolSchema
            compliance = schemas.BoolSchema
            fieldOfView = schemas.StrSchema
            targetA = schemas.StrSchema
            negate = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "id": id,
                "metamodel": metamodel,
                "terminator": terminator,
                "compliance": compliance,
                "fieldOfView": fieldOfView,
                "targetA": targetA,
                "negate": negate,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metamodel"]) -> 'Metamodel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminator"]) -> MetaOapg.properties.terminator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compliance"]) -> MetaOapg.properties.compliance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldOfView"]) -> MetaOapg.properties.fieldOfView: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetA"]) -> MetaOapg.properties.targetA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["negate"]) -> MetaOapg.properties.negate: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["terminator"], typing_extensions.Literal["compliance"], typing_extensions.Literal["fieldOfView"], typing_extensions.Literal["targetA"], typing_extensions.Literal["negate"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metamodel"]) -> typing.Union['Metamodel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminator"]) -> typing.Union[MetaOapg.properties.terminator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compliance"]) -> typing.Union[MetaOapg.properties.compliance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldOfView"]) -> typing.Union[MetaOapg.properties.fieldOfView, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetA"]) -> typing.Union[MetaOapg.properties.targetA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["negate"]) -> typing.Union[MetaOapg.properties.negate, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["terminator"], typing_extensions.Literal["compliance"], typing_extensions.Literal["fieldOfView"], typing_extensions.Literal["targetA"], typing_extensions.Literal["negate"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        metamodel: typing.Union['Metamodel', schemas.Unset] = schemas.unset,
        terminator: typing.Union[MetaOapg.properties.terminator, bool, schemas.Unset] = schemas.unset,
        compliance: typing.Union[MetaOapg.properties.compliance, bool, schemas.Unset] = schemas.unset,
        fieldOfView: typing.Union[MetaOapg.properties.fieldOfView, str, schemas.Unset] = schemas.unset,
        targetA: typing.Union[MetaOapg.properties.targetA, str, schemas.Unset] = schemas.unset,
        negate: typing.Union[MetaOapg.properties.negate, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TargetInFovCondition':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            metamodel=metamodel,
            terminator=terminator,
            compliance=compliance,
            fieldOfView=fieldOfView,
            targetA=targetA,
            negate=negate,
            _configuration=_configuration,
        )

from sedaro_base_client.model.metamodel import Metamodel
