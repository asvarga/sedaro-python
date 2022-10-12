# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_old.paths.models_branches_branch_id_system_geometry_body_frame_vectors_.post import CreateBodyFrameVector
from sedaro_old.paths.models_branches_branch_id_system_geometry_body_frame_vectors_block_id.delete import DeleteBodyFrameVector
from sedaro_old.paths.models_branches_branch_id_system_geometry_body_frame_vectors_block_id.patch import UpdateBodyFrameVector


class BodyFrameVectorApi(
    CreateBodyFrameVector,
    DeleteBodyFrameVector,
    UpdateBodyFrameVector,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
