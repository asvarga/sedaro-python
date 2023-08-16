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


class RectangularFieldOfView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "widthHalfAngle",
            "name",
            "heightHalfAngle",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class heightHalfAngle(
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
                            AngleFieldOfView146,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'heightHalfAngle':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class widthHalfAngle(
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
                            AngleFieldOfView147,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'widthHalfAngle':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            
            
            class attitude(
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
                            QuaternionBase306,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attitude':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class relativeAttitude(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'relativeAttitude':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class articulationAngles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'articulationAngles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            boresightBodyFrameVector = schemas.StrSchema
            
            
            class sensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sensors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            articulations = schemas.DictSchema
            
            
            class articulationModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'articulationModes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            heightBodyFrameVector = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "heightHalfAngle": heightHalfAngle,
                "widthHalfAngle": widthHalfAngle,
                "id": id,
                "attitude": attitude,
                "relativeAttitude": relativeAttitude,
                "articulationAngles": articulationAngles,
                "boresightBodyFrameVector": boresightBodyFrameVector,
                "sensors": sensors,
                "articulations": articulations,
                "articulationModes": articulationModes,
                "heightBodyFrameVector": heightBodyFrameVector,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    widthHalfAngle: MetaOapg.properties.widthHalfAngle
    name: MetaOapg.properties.name
    heightHalfAngle: MetaOapg.properties.heightHalfAngle
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["widthHalfAngle"]) -> MetaOapg.properties.widthHalfAngle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heightHalfAngle"]) -> MetaOapg.properties.heightHalfAngle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attitude"]) -> MetaOapg.properties.attitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relativeAttitude"]) -> MetaOapg.properties.relativeAttitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["articulationAngles"]) -> MetaOapg.properties.articulationAngles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boresightBodyFrameVector"]) -> MetaOapg.properties.boresightBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensors"]) -> MetaOapg.properties.sensors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["articulations"]) -> MetaOapg.properties.articulations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["articulationModes"]) -> MetaOapg.properties.articulationModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heightBodyFrameVector"]) -> MetaOapg.properties.heightBodyFrameVector: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["widthHalfAngle"], typing_extensions.Literal["name"], typing_extensions.Literal["heightHalfAngle"], typing_extensions.Literal["id"], typing_extensions.Literal["attitude"], typing_extensions.Literal["relativeAttitude"], typing_extensions.Literal["articulationAngles"], typing_extensions.Literal["boresightBodyFrameVector"], typing_extensions.Literal["sensors"], typing_extensions.Literal["articulations"], typing_extensions.Literal["articulationModes"], typing_extensions.Literal["heightBodyFrameVector"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["widthHalfAngle"]) -> MetaOapg.properties.widthHalfAngle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heightHalfAngle"]) -> MetaOapg.properties.heightHalfAngle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attitude"]) -> typing.Union[MetaOapg.properties.attitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relativeAttitude"]) -> typing.Union[MetaOapg.properties.relativeAttitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["articulationAngles"]) -> typing.Union[MetaOapg.properties.articulationAngles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["boresightBodyFrameVector"]) -> typing.Union[MetaOapg.properties.boresightBodyFrameVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensors"]) -> typing.Union[MetaOapg.properties.sensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["articulations"]) -> typing.Union[MetaOapg.properties.articulations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["articulationModes"]) -> typing.Union[MetaOapg.properties.articulationModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heightBodyFrameVector"]) -> typing.Union[MetaOapg.properties.heightBodyFrameVector, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["widthHalfAngle"], typing_extensions.Literal["name"], typing_extensions.Literal["heightHalfAngle"], typing_extensions.Literal["id"], typing_extensions.Literal["attitude"], typing_extensions.Literal["relativeAttitude"], typing_extensions.Literal["articulationAngles"], typing_extensions.Literal["boresightBodyFrameVector"], typing_extensions.Literal["sensors"], typing_extensions.Literal["articulations"], typing_extensions.Literal["articulationModes"], typing_extensions.Literal["heightBodyFrameVector"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        widthHalfAngle: typing.Union[MetaOapg.properties.widthHalfAngle, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        heightHalfAngle: typing.Union[MetaOapg.properties.heightHalfAngle, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        attitude: typing.Union[MetaOapg.properties.attitude, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        relativeAttitude: typing.Union[MetaOapg.properties.relativeAttitude, list, tuple, schemas.Unset] = schemas.unset,
        articulationAngles: typing.Union[MetaOapg.properties.articulationAngles, list, tuple, schemas.Unset] = schemas.unset,
        boresightBodyFrameVector: typing.Union[MetaOapg.properties.boresightBodyFrameVector, str, schemas.Unset] = schemas.unset,
        sensors: typing.Union[MetaOapg.properties.sensors, list, tuple, schemas.Unset] = schemas.unset,
        articulations: typing.Union[MetaOapg.properties.articulations, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        articulationModes: typing.Union[MetaOapg.properties.articulationModes, list, tuple, schemas.Unset] = schemas.unset,
        heightBodyFrameVector: typing.Union[MetaOapg.properties.heightBodyFrameVector, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'RectangularFieldOfView':
        return super().__new__(
            cls,
            *_args,
            widthHalfAngle=widthHalfAngle,
            name=name,
            heightHalfAngle=heightHalfAngle,
            id=id,
            attitude=attitude,
            relativeAttitude=relativeAttitude,
            articulationAngles=articulationAngles,
            boresightBodyFrameVector=boresightBodyFrameVector,
            sensors=sensors,
            articulations=articulations,
            articulationModes=articulationModes,
            heightBodyFrameVector=heightBodyFrameVector,
            _configuration=_configuration,
        )

from sedaro_base_client.model.angle_field_of_view146 import AngleFieldOfView146
from sedaro_base_client.model.angle_field_of_view147 import AngleFieldOfView147
from sedaro_base_client.model.quaternion_base306 import QuaternionBase306
