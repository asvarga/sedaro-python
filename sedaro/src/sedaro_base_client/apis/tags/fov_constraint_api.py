# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_fields_of_view_constraints_.post import CreateFovConstraint
from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_fields_of_view_constraints_block_id.delete import DeleteFovConstraint
from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_fields_of_view_constraints_block_id.patch import UpdateFovConstraint


class FOVConstraintApi(
    CreateFovConstraint,
    DeleteFovConstraint,
    UpdateFovConstraint,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
