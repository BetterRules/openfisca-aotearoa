#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file browses the country package to find tests written in the YAML format and runs them.
# It is usually not necessary to edit it.

import os

from nose.tools import nottest
from openfisca_core.tools.test_runner import generate_tests

from openfisca_country_template import CountryTaxBenefitSystem

nottest(generate_tests)

tax_benefit_system = CountryTaxBenefitSystem()


def test():
    tests_directory = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    test_generator = generate_tests(tax_benefit_system, tests_directory)

    for test in test_generator:
        yield test
