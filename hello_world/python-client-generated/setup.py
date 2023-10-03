# coding: utf-8

"""
    QuestionsAPI

     QuestionsAPI helps you do operations with the scraped data. 🚀  ## Questions  You will be able to:  * **Put questions** (Create & Update & batch). * **Read questions**. * **Search questions**.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="QuestionsAPI",
    author_email="",
    url="",
    keywords=["Swagger", "QuestionsAPI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
     QuestionsAPI helps you do operations with the scraped data. 🚀  ## Questions  You will be able to:  * **Put questions** (Create &amp; Update &amp; batch). * **Read questions**. * **Search questions**.   # noqa: E501
    """
)