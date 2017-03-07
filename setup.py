#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Country-Template',
    version='0.1.0',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description=u'Template of a tax and benefit system for OpenFisca',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 6.1.0.dev0, < 7.0',
        ],
    packages=find_packages(),
    test_suite='nose.collector',
    )
