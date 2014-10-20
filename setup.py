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
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
    ],
    packages=find_packages(),
    install_requires=required
)
