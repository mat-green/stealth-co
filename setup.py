#  -*- coding: utf-8 -*- 
'''
Created on 24 Jan 2016

@author:     Matthew Green

@copyright:  2016 New Edge Engineering Ltd. All rights reserved.

@license:    MIT
'''

NAME = "stealthco"
SUMMARY = "Technical Test"
DESCRIPTION = "Command line application that renders vectors as ascii characters."

import os
import pkg_resources

from datetime import datetime

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def required(fname):
    """Reads file to create array of required packages
    :param fname: File name to be read.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read().split('\n')


def version():
    """Generates version number from current year, month and build number"""
    try:
        # try and get the distribution version of packaged component
        distribution = pkg_resources.get_distribution(NAME)
        version = distribution.version
    except pkg_resources.DistributionNotFound:
        # try and generate version number from Thoughtworks Go environment attributes
        build = '%s' % os.getenv('BUILD_COUNT', '0')
        date = datetime.now()
        version = '%s.%s' % (date.strftime('%y.%m'), build) # YY.MM.BUILD_COUNT format
    return version


config = {
    "name" : NAME,
    "version" : version(),
    "namespace_packages" : [ ],
    "packages" : find_packages(exclude=[
                                         "*.tests", "*.tests.*", "tests.*", "tests",
                                         "*.ez_setup", "*.ez_setup.*", "ez_setup.*", "ez_setup",
                                         "*.examples", "*.examples.*", "examples.*", "examples",
                                       ]),
    "include_package_data" : True,
    "package_data" : {
                       "" : [ ],
                     },
    "data_files" : [],
    "scripts" : [ ],
    "entry_points" : { },
    "install_requires" : [  required('requires.txt') ],
    "tests_require" : [ required('requires-for-tests.txt') ],
    "test_suite" : 'nose.collector',
    "zip_safe" : False,

    # Metadata for upload to PyPI
    "author" : 'Matthew Green',
    "author_email" : "matthew@newedgeengineering.com",
    "description" : SUMMARY,
    "long_description" : DESCRIPTION,
    "classifiers" : [
                      "Programming Language :: Python",
                    ],
    "license" : "MIT",
    "keywords" : "",
    "url" : "",
}


setup(**config)