import imp
from pkgutil import ImpImporter

from setuptools import find_packages, setup

setup(
    name="sucellus",
    version=0.1,
    packages=find_packages()
)