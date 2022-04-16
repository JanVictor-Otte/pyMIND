from setuptools import find_packages
from setuptools import setup
import os

root_path = os.path.dirname(__file__)
require = open(os.path.join(root_path, 'requirements.txt')).readlines()

setup(
    name='pymind',
    version='1.0.0',
    url='https://gitlab.gwdg.de/hli1/pymind',
    description='Python implementation of Multiscale Nemirovski Dantzig Estimators',
    packages=find_packages(),

    install_requires=[require]
)