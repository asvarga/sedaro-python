# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.7.0
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


class TerrestrialVehicleUpdateInterface(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "blocks",
            "root",
            "delete",
        }
        
        class properties:
        
            @staticmethod
            def root() -> typing.Type['TerrestrialVehicleModelRoot']:
                return TerrestrialVehicleModelRoot
            
            
            class blocks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
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
                                    Antenna,
                                    ResistanceLoad,
                                    PowerLoad,
                                    WaypointPathWithSpeed,
                                    DataInterface,
                                    InternalDataInterface,
                                    ReceiveInterface,
                                    PassiveTransmitInterface,
                                    CooperativeTransmitInterface,
                                    DataMode,
                                    OperationalMode,
                                    StaticFieldOfViewArticulationMode,
                                    TrackingFieldOfViewArticulationMode,
                                    ScanFieldOfViewArticulationMode,
                                    DataStorage,
                                    LaserCommModule,
                                    DataType,
                                    LoadState,
                                    BatteryPack,
                                    BatteryCell,
                                    Modem,
                                    Subsystem,
                                    WaypointPathWithDuration,
                                    CompoundCondition,
                                    TimeCondition,
                                    ElapsedTimeCondition,
                                    SatelliteToSatelliteCondition,
                                    TargetGroupToSatelliteCondition,
                                    SameTargetMultiCondition,
                                    SatelliteToScalarCondition,
                                    TargetGroupToScalarCondition,
                                    TargetToScalarCondition,
                                    ComponentToScalarCondition,
                                    SatelliteToTargetCondition,
                                    TargetGroupToTargetCondition,
                                    TargetToTargetCondition,
                                    TargetGroupInFovCondition,
                                    VectorInFovCondition,
                                    TargetInFovCondition,
                                    BodyInFovCondition,
                                    TargetGroup,
                                    Sensor,
                                    PowerProcessor,
                                    BusRegulator,
                                    BodyFrameVector,
                                    LocalVector,
                                    CelestialVector,
                                    TargetGroupVector,
                                    TargetVector,
                                    TerrestrialAttitudeDynamics,
                                    WaypointPathWithTimestamps,
                                    DataBus,
                                    AreaTarget,
                                    GroundTarget,
                                    SpaceTarget,
                                    CelestialTarget,
                                    Component,
                                    DynamicallyLoadedComponent,
                                    CircularFieldOfView,
                                    RectangularFieldOfView,
                                    Battery,
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
                ) -> 'blocks':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class delete(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'delete':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "root": root,
                "blocks": blocks,
                "delete": delete,
            }
    
    blocks: MetaOapg.properties.blocks
    root: 'TerrestrialVehicleModelRoot'
    delete: MetaOapg.properties.delete
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["root"]) -> 'TerrestrialVehicleModelRoot': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blocks"]) -> MetaOapg.properties.blocks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete"]) -> MetaOapg.properties.delete: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["root", "blocks", "delete", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["root"]) -> 'TerrestrialVehicleModelRoot': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blocks"]) -> MetaOapg.properties.blocks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete"]) -> MetaOapg.properties.delete: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["root", "blocks", "delete", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        blocks: typing.Union[MetaOapg.properties.blocks, list, tuple, ],
        root: 'TerrestrialVehicleModelRoot',
        delete: typing.Union[MetaOapg.properties.delete, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TerrestrialVehicleUpdateInterface':
        return super().__new__(
            cls,
            *_args,
            blocks=blocks,
            root=root,
            delete=delete,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.antenna import Antenna
from sedaro_base_client.model.area_target import AreaTarget
from sedaro_base_client.model.battery import Battery
from sedaro_base_client.model.battery_cell import BatteryCell
from sedaro_base_client.model.battery_pack import BatteryPack
from sedaro_base_client.model.body_frame_vector import BodyFrameVector
from sedaro_base_client.model.body_in_fov_condition import BodyInFovCondition
from sedaro_base_client.model.bus_regulator import BusRegulator
from sedaro_base_client.model.celestial_target import CelestialTarget
from sedaro_base_client.model.celestial_vector import CelestialVector
from sedaro_base_client.model.circular_field_of_view import CircularFieldOfView
from sedaro_base_client.model.component import Component
from sedaro_base_client.model.component_to_scalar_condition import ComponentToScalarCondition
from sedaro_base_client.model.compound_condition import CompoundCondition
from sedaro_base_client.model.cooperative_transmit_interface import CooperativeTransmitInterface
from sedaro_base_client.model.data_bus import DataBus
from sedaro_base_client.model.data_interface import DataInterface
from sedaro_base_client.model.data_mode import DataMode
from sedaro_base_client.model.data_storage import DataStorage
from sedaro_base_client.model.data_type import DataType
from sedaro_base_client.model.dynamically_loaded_component import DynamicallyLoadedComponent
from sedaro_base_client.model.elapsed_time_condition import ElapsedTimeCondition
from sedaro_base_client.model.ground_target import GroundTarget
from sedaro_base_client.model.internal_data_interface import InternalDataInterface
from sedaro_base_client.model.laser_comm_module import LaserCommModule
from sedaro_base_client.model.load_state import LoadState
from sedaro_base_client.model.local_vector import LocalVector
from sedaro_base_client.model.modem import Modem
from sedaro_base_client.model.operational_mode import OperationalMode
from sedaro_base_client.model.passive_transmit_interface import PassiveTransmitInterface
from sedaro_base_client.model.power_load import PowerLoad
from sedaro_base_client.model.power_processor import PowerProcessor
from sedaro_base_client.model.receive_interface import ReceiveInterface
from sedaro_base_client.model.rectangular_field_of_view import RectangularFieldOfView
from sedaro_base_client.model.resistance_load import ResistanceLoad
from sedaro_base_client.model.same_target_multi_condition import SameTargetMultiCondition
from sedaro_base_client.model.satellite_to_satellite_condition import SatelliteToSatelliteCondition
from sedaro_base_client.model.satellite_to_scalar_condition import SatelliteToScalarCondition
from sedaro_base_client.model.satellite_to_target_condition import SatelliteToTargetCondition
from sedaro_base_client.model.scan_field_of_view_articulation_mode import ScanFieldOfViewArticulationMode
from sedaro_base_client.model.sensor import Sensor
from sedaro_base_client.model.space_target import SpaceTarget
from sedaro_base_client.model.static_field_of_view_articulation_mode import StaticFieldOfViewArticulationMode
from sedaro_base_client.model.subsystem import Subsystem
from sedaro_base_client.model.target_group import TargetGroup
from sedaro_base_client.model.target_group_in_fov_condition import TargetGroupInFovCondition
from sedaro_base_client.model.target_group_to_satellite_condition import TargetGroupToSatelliteCondition
from sedaro_base_client.model.target_group_to_scalar_condition import TargetGroupToScalarCondition
from sedaro_base_client.model.target_group_to_target_condition import TargetGroupToTargetCondition
from sedaro_base_client.model.target_group_vector import TargetGroupVector
from sedaro_base_client.model.target_in_fov_condition import TargetInFovCondition
from sedaro_base_client.model.target_to_scalar_condition import TargetToScalarCondition
from sedaro_base_client.model.target_to_target_condition import TargetToTargetCondition
from sedaro_base_client.model.target_vector import TargetVector
from sedaro_base_client.model.terrestrial_attitude_dynamics import TerrestrialAttitudeDynamics
from sedaro_base_client.model.terrestrial_vehicle_model_root import TerrestrialVehicleModelRoot
from sedaro_base_client.model.time_condition import TimeCondition
from sedaro_base_client.model.tracking_field_of_view_articulation_mode import TrackingFieldOfViewArticulationMode
from sedaro_base_client.model.vector_in_fov_condition import VectorInFovCondition
from sedaro_base_client.model.waypoint_path_with_duration import WaypointPathWithDuration
from sedaro_base_client.model.waypoint_path_with_speed import WaypointPathWithSpeed
from sedaro_base_client.model.waypoint_path_with_timestamps import WaypointPathWithTimestamps
