# Dia 27: https://www.youtube.com/watch?v=Zf9sN-w0BVE&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=36
# Distributed Packages

from setuptools import setup


setup(
    name = 'calculationspackage',
    version = '1.0.0',
    description = 'calculates round and power',
    author = 'Juan S',
    packages =['calculations','calculations.medium']
)