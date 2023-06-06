from config import API_KEY, HOST, SIMPLESAT_A_T_ID, SIMPLESAT_SCENARIO_ID
from sedaro_2 import SedaroApiClient
from sedaro_2.branch_clients.block_clients import Block, BlockType

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


# TODO: if update these lists, also update type hints of BranchClient
agent_template_blocks = [
    'AngularVelocitySensor',
    'Antenna',
    'AveragingAlgorithm',
    'Battery',
    'BatteryCell',
    'BatteryPack',
    'BodyFrameVector',
    'BodyInFovCondition',
    'BusRegulator',
    'CelestialTarget',
    'CelestialVector',
    'CircularFieldOfView',
    'Component',
    'ComponentToScalarCondition',
    'CompoundCondition',
    'Cooler',
    'CooperativeTransmitInterface',
    'DataBus',
    'DataInterface',
    'DataMode',
    'DataStorage',
    'DataType',
    'DirectionSensor',
    'EkfAlgorithm',
    'FixedSurface',
    'FuelReservoir',
    'FullyRegDetPowerProcessor',
    'GpsAlgorithm',
    'GroundTarget',
    'Heater',
    'InternalDataInterface',
    'LaserCommModule',
    'LoadState',
    'LocalVector',
    'LockPointingMode',
    'Magnetorquer',
    'MaxAlignPointingMode',
    'MekfAlgorithm',
    'Modem',
    'OperationalMode',
    'OpticalAttitudeSensor',
    'Orbit',
    'PassivePointingMode',
    'PassiveTransmitInterface',
    'PidAlgorithm',
    'PositionSensor',
    'PowerLoad',
    'PowerProcessor',
    'QuasiRegDetPowerProcessor',
    'ReactionWheel',
    'ReceiveInterface',
    'RectangularFieldOfView',
    'ResistanceLoad',
    'SameTargetMultiCondition',
    'Satellite',
    'SatelliteToSatelliteCondition',
    'SatelliteToScalarCondition',
    'SatelliteToTargetCondition',
    'SingleConvHybridPowerProcessor',
    'SingleConvMpptPowerProcessor',
    'SlidingModeAlgorithm',
    'SolarArray',
    'SolarCell',
    'SolarPanel',
    'SpaceTarget',
    'SphericalFuelTank',
    'SpherocylinderFuelTank',
    'StaticThrustControlAlgorithm',
    'Subsystem',
    'SunTrackingSurface',
    'SurfaceMaterial',
    'TargetGroup',
    'TargetGroupInFovCondition',
    'TargetGroupToSatelliteCondition',
    'TargetGroupToScalarCondition',
    'TargetGroupToTargetCondition',
    'TargetGroupVector',
    'TargetInFovCondition',
    'TargetToScalarCondition',
    'TargetToTargetCondition',
    'TargetVector',
    'TempControllerState',
    'ThermalInterface',
    'ThermalInterfaceMaterial',
    'Thruster',
    'TimeCondition',
    'TriadAlgorithm',
    'TwoConvMpptPowerProcessor',
    'VectorInFovCondition',
    'VectorSensor',
    'VectorTrackingSurface'
]

# TODO: if update these lists, also update type hints of BranchClient
scenario_blocks = [
    'Agent',
    'AgentGroup',
    'ClockConfig',
    'Orbit'
]


def test_block_class_client_options():
    for get_method, branch_id, blocks in [
        [sedaro.agent_template_branch, SIMPLESAT_A_T_ID, agent_template_blocks],
        [sedaro.scenario_branch, SIMPLESAT_SCENARIO_ID, scenario_blocks]
    ]:
        branch = get_method(branch_id)
        branch_blocks = sorted(branch.data['_block_names'])
        # CHECK: lists above are correct
        assert blocks == branch_blocks

        for block in branch_blocks:
            block_class_client: BlockType = getattr(branch, block)

            # CHECK: is a Block Class Client
            assert isinstance(block_class_client, BlockType)

            # CHECK: can use create method
            try:
                block_class_client.create()
            except Exception as e:
                assert isinstance(e, ValueError)
                assert 'Must provide fields' in str(e)

            # CHECK: can use get_all method
            all_blocks_of_type = block_class_client.get_all()
            assert type(all_blocks_of_type) == list
            if len(all_blocks_of_type):
                assert isinstance(all_blocks_of_type[0], Block)

        # CHECK: bad block class clients
        for bad_block in ['try_me', 'and_me', 'NO_wayYou_will_CatchMe!!!!!!']:
            try:
                getattr(branch, bad_block)
            except Exception as e:
                assert isinstance(e, AttributeError)
                assert f'Unable to create a "{BlockType.__name__}" from string: "{bad_block}".' in str(e)


def run_tests():
    test_block_class_client_options()
