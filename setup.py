#!/usr/bin/python3 -B

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup 

setup_args = generate_distutils_setup(
    version='0.0.0',
    packages=['ayspot_a1_hw'],
    package_dir={'': 'src'}
)

setup(**setup_args)
