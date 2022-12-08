# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sedaro_base_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_SATELLITE_BLOCK_ID = "/models/branches/{branchId}/system/satellite/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_GEOMETRY_BODYFRAMEVECTORS_ = "/models/branches/{branchId}/system/geometry/body-frame-vectors/"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_GEOMETRY_BODYFRAMEVECTORS_BLOCK_ID = "/models/branches/{branchId}/system/geometry/body-frame-vectors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_GEOMETRY_SURFACES_ = "/models/branches/{branchId}/system/geometry/surfaces/"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_GEOMETRY_SURFACES_BLOCK_ID = "/models/branches/{branchId}/system/geometry/surfaces/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_GEOMETRY_SURFACES_MATERIALS_ = "/models/branches/{branchId}/system/geometry/surfaces/materials/"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_GEOMETRY_SURFACES_MATERIALS_BLOCK_ID = "/models/branches/{branchId}/system/geometry/surfaces/materials/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_SUBSYSTEMS_ = "/models/branches/{branchId}/system/subsystems/"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_SUBSYSTEMS_BLOCK_ID = "/models/branches/{branchId}/system/subsystems/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_SUBSYSTEMS_COMPONENTS_ = "/models/branches/{branchId}/system/subsystems/components/"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_SUBSYSTEMS_COMPONENTS_BLOCK_ID = "/models/branches/{branchId}/system/subsystems/components/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_LOADS_ = "/models/branches/{branchId}/system/loads/"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_LOADS_BLOCK_ID = "/models/branches/{branchId}/system/loads/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_LOADS_STATES_ = "/models/branches/{branchId}/system/loads/states/"
    MODELS_BRANCHES_BRANCH_ID_SYSTEM_LOADS_STATES_BLOCK_ID = "/models/branches/{branchId}/system/loads/states/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_OPERATIONALMODES_ = "/models/branches/{branchId}/cdh/conops/operational-modes/"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_OPERATIONALMODES_BLOCK_ID = "/models/branches/{branchId}/cdh/conops/operational-modes/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_CONDITIONS_ = "/models/branches/{branchId}/cdh/conops/conditions/"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_CONDITIONS_BLOCK_ID = "/models/branches/{branchId}/cdh/conops/conditions/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_GROUPCONDITIONS_ = "/models/branches/{branchId}/cdh/conops/group-conditions/"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_GROUPCONDITIONS_BLOCK_ID = "/models/branches/{branchId}/cdh/conops/group-conditions/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_SPACETARGETS_ = "/models/branches/{branchId}/cdh/conops/space-targets/"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_SPACETARGETS_BLOCK_ID = "/models/branches/{branchId}/cdh/conops/space-targets/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_CELESTIALTARGETS_ = "/models/branches/{branchId}/cdh/conops/celestial-targets/"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_CELESTIALTARGETS_BLOCK_ID = "/models/branches/{branchId}/cdh/conops/celestial-targets/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_GROUNDTARGETS_ = "/models/branches/{branchId}/cdh/conops/ground-targets/"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_GROUNDTARGETS_BLOCK_ID = "/models/branches/{branchId}/cdh/conops/ground-targets/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_TARGETGROUPS_ = "/models/branches/{branchId}/cdh/conops/target-groups/"
    MODELS_BRANCHES_BRANCH_ID_CDH_CONOPS_TARGETGROUPS_BLOCK_ID = "/models/branches/{branchId}/cdh/conops/target-groups/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_SOLARARRAYS_ = "/models/branches/{branchId}/power/solar-arrays/"
    MODELS_BRANCHES_BRANCH_ID_POWER_SOLARARRAYS_BLOCK_ID = "/models/branches/{branchId}/power/solar-arrays/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_SOLARARRAYS_PANELS_ = "/models/branches/{branchId}/power/solar-arrays/panels/"
    MODELS_BRANCHES_BRANCH_ID_POWER_SOLARARRAYS_PANELS_BLOCK_ID = "/models/branches/{branchId}/power/solar-arrays/panels/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_SOLARARRAYS_CELLS_ = "/models/branches/{branchId}/power/solar-arrays/cells/"
    MODELS_BRANCHES_BRANCH_ID_POWER_SOLARARRAYS_CELLS_BLOCK_ID = "/models/branches/{branchId}/power/solar-arrays/cells/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_BATTERIES_BLOCK_ID = "/models/branches/{branchId}/power/batteries/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_BATTERIES_PACKS_ = "/models/branches/{branchId}/power/batteries/packs/"
    MODELS_BRANCHES_BRANCH_ID_POWER_BATTERIES_PACKS_BLOCK_ID = "/models/branches/{branchId}/power/batteries/packs/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_BATTERIES_CELLS_ = "/models/branches/{branchId}/power/batteries/cells/"
    MODELS_BRANCHES_BRANCH_ID_POWER_BATTERIES_CELLS_BLOCK_ID = "/models/branches/{branchId}/power/batteries/cells/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_EPS_TOPOLOGY_BLOCK_ID = "/models/branches/{branchId}/power/eps/topology/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_POWER_EPS_BUSREGULATORS_ = "/models/branches/{branchId}/power/eps/bus-regulators/"
    MODELS_BRANCHES_BRANCH_ID_POWER_EPS_BUSREGULATORS_BLOCK_ID = "/models/branches/{branchId}/power/eps/bus-regulators/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_TEMPCONTROLLERS_HEATERS_ = "/models/branches/{branchId}/thermal/temp-controllers/heaters/"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_TEMPCONTROLLERS_HEATERS_BLOCK_ID = "/models/branches/{branchId}/thermal/temp-controllers/heaters/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_TEMPCONTROLLERS_COOLERS_ = "/models/branches/{branchId}/thermal/temp-controllers/coolers/"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_TEMPCONTROLLERS_COOLERS_BLOCK_ID = "/models/branches/{branchId}/thermal/temp-controllers/coolers/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_TEMPCONTROLLERS_STATES_ = "/models/branches/{branchId}/thermal/temp-controllers/states/"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_TEMPCONTROLLERS_STATES_BLOCK_ID = "/models/branches/{branchId}/thermal/temp-controllers/states/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_THERMALINTERFACES_ = "/models/branches/{branchId}/thermal/thermal-interfaces/"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_THERMALINTERFACES_BLOCK_ID = "/models/branches/{branchId}/thermal/thermal-interfaces/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_THERMALINTERFACEMATERIALS_ = "/models/branches/{branchId}/thermal/thermal-interface-materials/"
    MODELS_BRANCHES_BRANCH_ID_THERMAL_THERMALINTERFACEMATERIALS_BLOCK_ID = "/models/branches/{branchId}/thermal/thermal-interface-materials/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_POINTINGMODES_PASSIVE_ = "/models/branches/{branchId}/gnc/pointing-modes/passive/"
    MODELS_BRANCHES_BRANCH_ID_GNC_POINTINGMODES_PASSIVE_BLOCK_ID = "/models/branches/{branchId}/gnc/pointing-modes/passive/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_POINTINGMODES_LOCK_ = "/models/branches/{branchId}/gnc/pointing-modes/lock/"
    MODELS_BRANCHES_BRANCH_ID_GNC_POINTINGMODES_LOCK_BLOCK_ID = "/models/branches/{branchId}/gnc/pointing-modes/lock/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_POINTINGMODES_MAXSECONDARYALIGN_ = "/models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/"
    MODELS_BRANCHES_BRANCH_ID_GNC_POINTINGMODES_MAXSECONDARYALIGN_BLOCK_ID = "/models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_LOCALVECTORS_ = "/models/branches/{branchId}/gnc/reference-vectors/local-vectors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_LOCALVECTORS_BLOCK_ID = "/models/branches/{branchId}/gnc/reference-vectors/local-vectors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_CELESTIALVECTORS_ = "/models/branches/{branchId}/gnc/reference-vectors/celestial-vectors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_CELESTIALVECTORS_BLOCK_ID = "/models/branches/{branchId}/gnc/reference-vectors/celestial-vectors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_TARGETVECTORS_ = "/models/branches/{branchId}/gnc/reference-vectors/target-vectors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_TARGETVECTORS_BLOCK_ID = "/models/branches/{branchId}/gnc/reference-vectors/target-vectors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_TARGETGROUPVECTORS_ = "/models/branches/{branchId}/gnc/reference-vectors/target-group-vectors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_REFERENCEVECTORS_TARGETGROUPVECTORS_BLOCK_ID = "/models/branches/{branchId}/gnc/reference-vectors/target-group-vectors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_DIRECTIONSENSORS_ = "/models/branches/{branchId}/gnc/sensors/direction-sensors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_DIRECTIONSENSORS_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/direction-sensors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_VECTORSENSORS_ = "/models/branches/{branchId}/gnc/sensors/vector-sensors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_VECTORSENSORS_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/vector-sensors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_OPTICALATTITUDESENSORS_ = "/models/branches/{branchId}/gnc/sensors/optical-attitude-sensors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_OPTICALATTITUDESENSORS_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/optical-attitude-sensors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_POSITIONSENSORS_ = "/models/branches/{branchId}/gnc/sensors/position-sensors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_POSITIONSENSORS_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/position-sensors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_ANGULARVELOCITYSENSORS_ = "/models/branches/{branchId}/gnc/sensors/angular-velocity-sensors/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_ANGULARVELOCITYSENSORS_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/angular-velocity-sensors/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_FIELDSOFVIEW_CIRCFIELDSOFVIEW_ = "/models/branches/{branchId}/gnc/sensors/fields-of-view/circ-fields-of-view/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_FIELDSOFVIEW_CIRCFIELDSOFVIEW_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/fields-of-view/circ-fields-of-view/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_FIELDSOFVIEW_RECTFIELDSOFVIEW_ = "/models/branches/{branchId}/gnc/sensors/fields-of-view/rect-fields-of-view/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_FIELDSOFVIEW_RECTFIELDSOFVIEW_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/fields-of-view/rect-fields-of-view/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_FIELDSOFVIEW_CONSTRAINTS_ = "/models/branches/{branchId}/gnc/sensors/fields-of-view/constraints/"
    MODELS_BRANCHES_BRANCH_ID_GNC_SENSORS_FIELDSOFVIEW_CONSTRAINTS_BLOCK_ID = "/models/branches/{branchId}/gnc/sensors/fields-of-view/constraints/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ACTUATORS_MAGNETORQUERS_ = "/models/branches/{branchId}/gnc/actuators/magnetorquers/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ACTUATORS_MAGNETORQUERS_BLOCK_ID = "/models/branches/{branchId}/gnc/actuators/magnetorquers/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ACTUATORS_REACTIONWHEELS_ = "/models/branches/{branchId}/gnc/actuators/reaction-wheels/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ACTUATORS_REACTIONWHEELS_BLOCK_ID = "/models/branches/{branchId}/gnc/actuators/reaction-wheels/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDEDETERMINATION_TRIAD_ = "/models/branches/{branchId}/gnc/algorithms/attitude-determination/triad/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDEDETERMINATION_TRIAD_BLOCK_ID = "/models/branches/{branchId}/gnc/algorithms/attitude-determination/triad/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDEDETERMINATION_AVERAGING_ = "/models/branches/{branchId}/gnc/algorithms/attitude-determination/averaging/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDEDETERMINATION_AVERAGING_BLOCK_ID = "/models/branches/{branchId}/gnc/algorithms/attitude-determination/averaging/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDEDETERMINATION_MEKF_ = "/models/branches/{branchId}/gnc/algorithms/attitude-determination/mekf/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDEDETERMINATION_MEKF_BLOCK_ID = "/models/branches/{branchId}/gnc/algorithms/attitude-determination/mekf/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ORBITDETERMINATION_EKF_ = "/models/branches/{branchId}/gnc/algorithms/orbit-determination/ekf/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ORBITDETERMINATION_EKF_BLOCK_ID = "/models/branches/{branchId}/gnc/algorithms/orbit-determination/ekf/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ORBITDETERMINATION_GPS_ = "/models/branches/{branchId}/gnc/algorithms/orbit-determination/gps/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ORBITDETERMINATION_GPS_BLOCK_ID = "/models/branches/{branchId}/gnc/algorithms/orbit-determination/gps/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDECONTROL_SLIDINGMODE_ = "/models/branches/{branchId}/gnc/algorithms/attitude-control/sliding-mode/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDECONTROL_SLIDINGMODE_BLOCK_ID = "/models/branches/{branchId}/gnc/algorithms/attitude-control/sliding-mode/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDECONTROL_PID_ = "/models/branches/{branchId}/gnc/algorithms/attitude-control/pid/"
    MODELS_BRANCHES_BRANCH_ID_GNC_ALGORITHMS_ATTITUDECONTROL_PID_BLOCK_ID = "/models/branches/{branchId}/gnc/algorithms/attitude-control/pid/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_AGENTS_ = "/models/branches/{branchId}/agents/"
    MODELS_BRANCHES_BRANCH_ID_AGENTS_BLOCK_ID = "/models/branches/{branchId}/agents/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_CLOCKCONFIGS_ = "/models/branches/{branchId}/clock-configs/"
    MODELS_BRANCHES_BRANCH_ID_CLOCKCONFIGS_BLOCK_ID = "/models/branches/{branchId}/clock-configs/{blockId}"
    MODELS_BRANCHES_BRANCH_ID_ORBITS_ = "/models/branches/{branchId}/orbits/"
    MODELS_BRANCHES_BRANCH_ID_ORBITS_BLOCK_ID = "/models/branches/{branchId}/orbits/{blockId}"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_ = "/simulations/branches/{branchId}/control/"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_JOB_ID = "/simulations/branches/{branchId}/control/{jobId}"
    DATA_ = "/data/"
    MODELS_BRANCHES_BRANCH_ID = "/models/branches/{branchId}"
    MODELS_BRANCHES_BRANCH_IDSHAREAUTH_ = "/models/branches/{branchId}share-auth/"
    MODELS_BRANCHES_BRANCH_IDCOMMITS_ = "/models/branches/{branchId}commits/"
    MODELS_BRANCHES_CURRENT_BRANCH_ID_MERGE_INCOMING_BRANCH_ID = "/models/branches/{currentBranchId}/merge/{incomingBranchId}"
    MODELS_BRANCHES_BRANCH_IDCOMMITTED_ = "/models/branches/{branchId}committed/"
    MODELS_BRANCHES_BRANCH_IDSAVED_ = "/models/branches/{branchId}saved/"
