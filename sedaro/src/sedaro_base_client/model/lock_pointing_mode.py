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


class LockPointingMode(
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
            odAlgorithm = schemas.StrSchema
            adAlgorithm = schemas.StrSchema
            tcAlgorithm = schemas.StrSchema
            
            
            class reactionWheelCommands(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'reactionWheelCommands':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class magnetorquerCommands(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'magnetorquerCommands':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            commandedAttitude = schemas.AnyTypeSchema
            commandedAngularRates = schemas.AnyTypeSchema
            lockBodyFrameVector = schemas.StrSchema
            lockVector = schemas.StrSchema
            acAlgorithm = schemas.StrSchema
            
            
            class spinRate(
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
                            AngularVelocityBase199,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'spinRate':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "name": name,
                "id": id,
                "metamodel": metamodel,
                "odAlgorithm": odAlgorithm,
                "adAlgorithm": adAlgorithm,
                "tcAlgorithm": tcAlgorithm,
                "reactionWheelCommands": reactionWheelCommands,
                "magnetorquerCommands": magnetorquerCommands,
                "commandedAttitude": commandedAttitude,
                "commandedAngularRates": commandedAngularRates,
                "lockBodyFrameVector": lockBodyFrameVector,
                "lockVector": lockVector,
                "acAlgorithm": acAlgorithm,
                "spinRate": spinRate,
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
    def __getitem__(self, name: typing_extensions.Literal["odAlgorithm"]) -> MetaOapg.properties.odAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adAlgorithm"]) -> MetaOapg.properties.adAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tcAlgorithm"]) -> MetaOapg.properties.tcAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactionWheelCommands"]) -> MetaOapg.properties.reactionWheelCommands: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["magnetorquerCommands"]) -> MetaOapg.properties.magnetorquerCommands: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedAttitude"]) -> MetaOapg.properties.commandedAttitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedAngularRates"]) -> MetaOapg.properties.commandedAngularRates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> MetaOapg.properties.lockBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockVector"]) -> MetaOapg.properties.lockVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acAlgorithm"]) -> MetaOapg.properties.acAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spinRate"]) -> MetaOapg.properties.spinRate: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["odAlgorithm"], typing_extensions.Literal["adAlgorithm"], typing_extensions.Literal["tcAlgorithm"], typing_extensions.Literal["reactionWheelCommands"], typing_extensions.Literal["magnetorquerCommands"], typing_extensions.Literal["commandedAttitude"], typing_extensions.Literal["commandedAngularRates"], typing_extensions.Literal["lockBodyFrameVector"], typing_extensions.Literal["lockVector"], typing_extensions.Literal["acAlgorithm"], typing_extensions.Literal["spinRate"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metamodel"]) -> typing.Union['Metamodel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["odAlgorithm"]) -> typing.Union[MetaOapg.properties.odAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adAlgorithm"]) -> typing.Union[MetaOapg.properties.adAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tcAlgorithm"]) -> typing.Union[MetaOapg.properties.tcAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactionWheelCommands"]) -> typing.Union[MetaOapg.properties.reactionWheelCommands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["magnetorquerCommands"]) -> typing.Union[MetaOapg.properties.magnetorquerCommands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedAttitude"]) -> typing.Union[MetaOapg.properties.commandedAttitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedAngularRates"]) -> typing.Union[MetaOapg.properties.commandedAngularRates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> typing.Union[MetaOapg.properties.lockBodyFrameVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockVector"]) -> typing.Union[MetaOapg.properties.lockVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acAlgorithm"]) -> typing.Union[MetaOapg.properties.acAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spinRate"]) -> typing.Union[MetaOapg.properties.spinRate, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["odAlgorithm"], typing_extensions.Literal["adAlgorithm"], typing_extensions.Literal["tcAlgorithm"], typing_extensions.Literal["reactionWheelCommands"], typing_extensions.Literal["magnetorquerCommands"], typing_extensions.Literal["commandedAttitude"], typing_extensions.Literal["commandedAngularRates"], typing_extensions.Literal["lockBodyFrameVector"], typing_extensions.Literal["lockVector"], typing_extensions.Literal["acAlgorithm"], typing_extensions.Literal["spinRate"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        metamodel: typing.Union['Metamodel', schemas.Unset] = schemas.unset,
        odAlgorithm: typing.Union[MetaOapg.properties.odAlgorithm, str, schemas.Unset] = schemas.unset,
        adAlgorithm: typing.Union[MetaOapg.properties.adAlgorithm, str, schemas.Unset] = schemas.unset,
        tcAlgorithm: typing.Union[MetaOapg.properties.tcAlgorithm, str, schemas.Unset] = schemas.unset,
        reactionWheelCommands: typing.Union[MetaOapg.properties.reactionWheelCommands, list, tuple, schemas.Unset] = schemas.unset,
        magnetorquerCommands: typing.Union[MetaOapg.properties.magnetorquerCommands, list, tuple, schemas.Unset] = schemas.unset,
        commandedAttitude: typing.Union[MetaOapg.properties.commandedAttitude, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        commandedAngularRates: typing.Union[MetaOapg.properties.commandedAngularRates, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        lockBodyFrameVector: typing.Union[MetaOapg.properties.lockBodyFrameVector, str, schemas.Unset] = schemas.unset,
        lockVector: typing.Union[MetaOapg.properties.lockVector, str, schemas.Unset] = schemas.unset,
        acAlgorithm: typing.Union[MetaOapg.properties.acAlgorithm, str, schemas.Unset] = schemas.unset,
        spinRate: typing.Union[MetaOapg.properties.spinRate, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LockPointingMode':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            metamodel=metamodel,
            odAlgorithm=odAlgorithm,
            adAlgorithm=adAlgorithm,
            tcAlgorithm=tcAlgorithm,
            reactionWheelCommands=reactionWheelCommands,
            magnetorquerCommands=magnetorquerCommands,
            commandedAttitude=commandedAttitude,
            commandedAngularRates=commandedAngularRates,
            lockBodyFrameVector=lockBodyFrameVector,
            lockVector=lockVector,
            acAlgorithm=acAlgorithm,
            spinRate=spinRate,
            _configuration=_configuration,
        )

from sedaro_base_client.model.angular_velocity_base199 import AngularVelocityBase199
from sedaro_base_client.model.metamodel import Metamodel
