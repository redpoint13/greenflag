# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='greenflag',
    version='0.0.1',
    description='Green Flags',
    long_description=readme,
    author='Tony Shouse',
    author_email='redpoint13@gmail.com  ',
    url='https://github.com/redpoint13/greenflag.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

