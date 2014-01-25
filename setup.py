#!/usr/bin/env python

"""
Setup
"""

from distutils.core import setup


setup(
    name='Python Check Unassigned Unicode',
    version='1.0',
    description='Check for unassigned unicode in python',
    author='Brendon Crawford',
    author_email='brendon at stockr dot com',
    url='https://github.com/stockr-labs/python_check_unassigned_unicode',
    packages=['check_unassigned_unicode'],
    package_dir = {'': 'src'}
)

