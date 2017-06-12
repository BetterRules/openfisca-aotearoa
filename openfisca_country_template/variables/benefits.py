# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See https://doc.openfisca.fr/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class basic_income(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = "Basic income provided to adults"
    url = "https://law.gov.example/basic_income"  # Always use the most official source

    # Since Dec 1st 2016, the basic income is provided to any adult, without considering their income.
    def formula_2016_12(person, period, legislation):
        age_condition = person('age', period) >= legislation(period).general.age_of_majority
        return age_condition * legislation(period).benefits.basic_income  # This '*' is a vectorial 'if'. See https://doc.openfisca.fr/coding-the-legislation/30_case_disjunction.html#simple-multiplication

    # From Dec 1st 2015 to Nov 30 2016, the basic income is provided to adults who have no income.
    # Before Dec 1st 2015, the basic income does not exist in the law, and calculating it returns its default value, which is 0.
    def formula_2015_12(person, period, legislation):
        age_condition = person('age', period) >= legislation(period).general.age_of_majority
        salary_condition = person('salary', period) == 0
        return age_condition * salary_condition * legislation(period).benefits.basic_income  # The '*' is also used as a vectorial 'and'. See https://doc.openfisca.fr/coding-the-legislation/25_vectorial_computing.html#forbidden-operations-and-alternatives


class housing_allowance(Variable):
    column = FloatCol
    entity = Household
    definition_period = MONTH
    label = "Housing allowange"
    url = "https://law.gov.example/housing_allowance"  # Always use the most official source
    end = '2016-11-30'  # This allowance was removed on the 1st of Dec 2016. Calculating it before this date will always return the variable default value, 0.

    # This allowance was introduced on the 1st of Jan 1980. Calculating it before this date will always return the variable default value, 0.
    def formula_1980(household, period, legislation):
        return household('rent', period) * legislation(period).benefits.housing_allowance
