#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created based on: https://github.com/kennethreitz/setup.py/blob/master/setup.py
# Alternative: https://github.com/seanfisk/python-project-template/blob/master/setup.py.tpl
import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'utils'
MAIN_PACKAGE = 'utils'  # Change if main package != NAME
DESCRIPTION = 'Utility functionality for training.'
URL = ''
EMAIL = 'oliver.atanaszov@gmail.com'
AUTHOR = 'Oliver Atanaszov'
REQUIRES_PYTHON = '>=3.6'
VERSION = None  # Only set version if you like to overwrite the version in __version__.py

# Please define the requirements within the requirements.txt

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

# Check if version is right
if sys.version_info[:1] == 2 or (sys.version_info[:1] == 3 and sys.version_info[:2] < (3, 6)):
    raise Exception('This package needs Python 3.6 or later.')

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!

try:
    # convert markdown to rst format
    import pypandoc
    long_description = pypandoc.convert(here, 'README.md', 'rst')
    long_description = long_description.replace("\r", "")
except:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()

# Read the requirements.txt and use it as the setup.py requirements
with io.open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.rstrip() for line in f.readlines()]

setup(
    name=NAME,
    version="0.0.1",
    description=DESCRIPTION,
    long_description="%s\n\nRequirements:\n%s" % (long_description, requirements),
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        # TODO: update this list to match your application: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
