# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "sedaro_old"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.15",
  "certifi",
  "python-dateutil",
  "frozendict >= 2.0.3",
  "typing_extensions",
]

setup(
    name=NAME,
    version=VERSION,
    description="Sedaro Satellite API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://gitlab.sedaro.com/sedaro-satellite/clients",
    keywords=["OpenAPI", "OpenAPI-Generator", "Sedaro Satellite API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501
    """
)
