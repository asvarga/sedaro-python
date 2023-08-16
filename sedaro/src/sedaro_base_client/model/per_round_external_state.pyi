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


class PerRoundExternalState(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "engineIndex",
        }
        
        class properties:
            engineIndex = schemas.IntSchema
            id = schemas.StrSchema
            
            
            class consumed(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            any_of_0 = schemas.StrSchema
                            any_of_1 = schemas.DictSchema
                            
                            @classmethod
                            @functools.lru_cache()
                            def any_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.any_of_0,
                                    cls.any_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'consumed':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class produced(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            any_of_0 = schemas.StrSchema
                            any_of_1 = schemas.DictSchema
                            
                            @classmethod
                            @functools.lru_cache()
                            def any_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.any_of_0,
                                    cls.any_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'produced':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class agents(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agents':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "engineIndex": engineIndex,
                "id": id,
                "consumed": consumed,
                "produced": produced,
                "agents": agents,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    engineIndex: MetaOapg.properties.engineIndex
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["engineIndex"]) -> MetaOapg.properties.engineIndex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consumed"]) -> MetaOapg.properties.consumed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["produced"]) -> MetaOapg.properties.produced: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agents"]) -> MetaOapg.properties.agents: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["engineIndex"], typing_extensions.Literal["id"], typing_extensions.Literal["consumed"], typing_extensions.Literal["produced"], typing_extensions.Literal["agents"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["engineIndex"]) -> MetaOapg.properties.engineIndex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consumed"]) -> typing.Union[MetaOapg.properties.consumed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["produced"]) -> typing.Union[MetaOapg.properties.produced, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agents"]) -> typing.Union[MetaOapg.properties.agents, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["engineIndex"], typing_extensions.Literal["id"], typing_extensions.Literal["consumed"], typing_extensions.Literal["produced"], typing_extensions.Literal["agents"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        engineIndex: typing.Union[MetaOapg.properties.engineIndex, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        consumed: typing.Union[MetaOapg.properties.consumed, list, tuple, schemas.Unset] = schemas.unset,
        produced: typing.Union[MetaOapg.properties.produced, list, tuple, schemas.Unset] = schemas.unset,
        agents: typing.Union[MetaOapg.properties.agents, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PerRoundExternalState':
        return super().__new__(
            cls,
            *_args,
            engineIndex=engineIndex,
            id=id,
            consumed=consumed,
            produced=produced,
            agents=agents,
            _configuration=_configuration,
        )
