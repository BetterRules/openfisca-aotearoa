#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='OpenFisca-Aotearoa',
    version='4.0.1',
    author='Service Innovation Lab',
    author_email='hamish.fraser@dia.govt.nz',
    description=u'Aotearoa New Zealand’s legislation as code project, utilising OpenFisca',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/ServiceInnovationLab/openfisca-aotearoa',
    include_package_data=True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 22, < 23.0',
        ],
    extras_require={
        'api': [
            'OpenFisca-Web-API >= 4.0.0, < 7.0',
            ],
        'test': [
            'flake8 >= 3.4.0, < 3.5.0',
            'flake8-print',
            'nose',
            ]
        },
    packages=find_packages(),
    test_suite='nose.collector',
    )
