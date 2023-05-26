# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.1.1
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


class Orbit(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class initialStateDefType(
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
                            InitialStateDefType,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'initialStateDefType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class initialStateDefParams(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
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
                            StateVector,
                            ClassicalOrbitalElements,
                            Tle,
                            IssReferenceOrbit,
                            GeostationaryReferenceOrbit,
                            GeostationaryTransferReferenceOrbit,
                            PolarCircularReferenceOrbit,
                            EquatorialCircularReferenceOrbit,
                            SunSynchronousCircularOrbit,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'initialStateDefParams':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def orbitalElements() -> typing.Type['OrbitalElementsData']:
                return OrbitalElementsData
            period = schemas.NumberSchema
            semiLatusRectum = schemas.NumberSchema
            radiusPerigee = schemas.NumberSchema
            
            
            class shadow(
                schemas.NumberSchema
            ):
                pass
            
            
            class beta(
                schemas.NumberSchema
            ):
                pass
            
            
            class magneticFieldVector(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'magneticFieldVector':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            atmosphericDensity = schemas.NumberSchema
            
            
            class lst(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "id": id,
                "initialStateDefType": initialStateDefType,
                "initialStateDefParams": initialStateDefParams,
                "orbitalElements": orbitalElements,
                "period": period,
                "semiLatusRectum": semiLatusRectum,
                "radiusPerigee": radiusPerigee,
                "shadow": shadow,
                "beta": beta,
                "magneticFieldVector": magneticFieldVector,
                "atmosphericDensity": atmosphericDensity,
                "lst": lst,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialStateDefType"]) -> MetaOapg.properties.initialStateDefType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialStateDefParams"]) -> MetaOapg.properties.initialStateDefParams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orbitalElements"]) -> 'OrbitalElementsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["period"]) -> MetaOapg.properties.period: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["semiLatusRectum"]) -> MetaOapg.properties.semiLatusRectum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radiusPerigee"]) -> MetaOapg.properties.radiusPerigee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shadow"]) -> MetaOapg.properties.shadow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beta"]) -> MetaOapg.properties.beta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["magneticFieldVector"]) -> MetaOapg.properties.magneticFieldVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["atmosphericDensity"]) -> MetaOapg.properties.atmosphericDensity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lst"]) -> MetaOapg.properties.lst: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["initialStateDefType"], typing_extensions.Literal["initialStateDefParams"], typing_extensions.Literal["orbitalElements"], typing_extensions.Literal["period"], typing_extensions.Literal["semiLatusRectum"], typing_extensions.Literal["radiusPerigee"], typing_extensions.Literal["shadow"], typing_extensions.Literal["beta"], typing_extensions.Literal["magneticFieldVector"], typing_extensions.Literal["atmosphericDensity"], typing_extensions.Literal["lst"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialStateDefType"]) -> typing.Union[MetaOapg.properties.initialStateDefType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialStateDefParams"]) -> typing.Union[MetaOapg.properties.initialStateDefParams, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orbitalElements"]) -> typing.Union['OrbitalElementsData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["period"]) -> typing.Union[MetaOapg.properties.period, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["semiLatusRectum"]) -> typing.Union[MetaOapg.properties.semiLatusRectum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radiusPerigee"]) -> typing.Union[MetaOapg.properties.radiusPerigee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shadow"]) -> typing.Union[MetaOapg.properties.shadow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beta"]) -> typing.Union[MetaOapg.properties.beta, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["magneticFieldVector"]) -> typing.Union[MetaOapg.properties.magneticFieldVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["atmosphericDensity"]) -> typing.Union[MetaOapg.properties.atmosphericDensity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lst"]) -> typing.Union[MetaOapg.properties.lst, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["initialStateDefType"], typing_extensions.Literal["initialStateDefParams"], typing_extensions.Literal["orbitalElements"], typing_extensions.Literal["period"], typing_extensions.Literal["semiLatusRectum"], typing_extensions.Literal["radiusPerigee"], typing_extensions.Literal["shadow"], typing_extensions.Literal["beta"], typing_extensions.Literal["magneticFieldVector"], typing_extensions.Literal["atmosphericDensity"], typing_extensions.Literal["lst"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        initialStateDefType: typing.Union[MetaOapg.properties.initialStateDefType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        initialStateDefParams: typing.Union[MetaOapg.properties.initialStateDefParams, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        orbitalElements: typing.Union['OrbitalElementsData', schemas.Unset] = schemas.unset,
        period: typing.Union[MetaOapg.properties.period, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        semiLatusRectum: typing.Union[MetaOapg.properties.semiLatusRectum, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        radiusPerigee: typing.Union[MetaOapg.properties.radiusPerigee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        shadow: typing.Union[MetaOapg.properties.shadow, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        beta: typing.Union[MetaOapg.properties.beta, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        magneticFieldVector: typing.Union[MetaOapg.properties.magneticFieldVector, list, tuple, schemas.Unset] = schemas.unset,
        atmosphericDensity: typing.Union[MetaOapg.properties.atmosphericDensity, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lst: typing.Union[MetaOapg.properties.lst, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Orbit':
        return super().__new__(
            cls,
            *_args,
            id=id,
            initialStateDefType=initialStateDefType,
            initialStateDefParams=initialStateDefParams,
            orbitalElements=orbitalElements,
            period=period,
            semiLatusRectum=semiLatusRectum,
            radiusPerigee=radiusPerigee,
            shadow=shadow,
            beta=beta,
            magneticFieldVector=magneticFieldVector,
            atmosphericDensity=atmosphericDensity,
            lst=lst,
            _configuration=_configuration,
        )

from sedaro_base_client.model.classical_orbital_elements import ClassicalOrbitalElements
from sedaro_base_client.model.equatorial_circular_reference_orbit import EquatorialCircularReferenceOrbit
from sedaro_base_client.model.geostationary_reference_orbit import GeostationaryReferenceOrbit
from sedaro_base_client.model.geostationary_transfer_reference_orbit import GeostationaryTransferReferenceOrbit
from sedaro_base_client.model.initial_state_def_type import InitialStateDefType
from sedaro_base_client.model.iss_reference_orbit import IssReferenceOrbit
from sedaro_base_client.model.orbital_elements_data import OrbitalElementsData
from sedaro_base_client.model.polar_circular_reference_orbit import PolarCircularReferenceOrbit
from sedaro_base_client.model.state_vector import StateVector
from sedaro_base_client.model.sun_synchronous_circular_orbit import SunSynchronousCircularOrbit
from sedaro_base_client.model.tle import Tle
