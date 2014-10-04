#!/usr/bin/env python

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='mathml-to-image-service',
    version='1.0',
    description='MathML to Image converter',
    author='',
    author_email='',
    url='https://github.com/rudigiesler/mathml-to-image-service/',
    packages=find_packages(),
    install_requires=required
)
