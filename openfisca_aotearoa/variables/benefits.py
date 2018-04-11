# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class basic_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Basic income provided to adults"
    reference = "https://law.gov.example/basic_income"  # Always use the most official source

    # Since Dec 1st 2016, the basic income is provided to any adult, without considering their income.
    def formula_2016_12(person, period, parameters):
        age_condition = person('age', period) >= parameters(period).general.age_of_majority
        return age_condition * parameters(period).benefits.basic_income  # This '*' is a vectorial 'if'. See http://openfisca.org/doc/coding-the-legislation/30_case_disjunction.html#simple-multiplication

    # From Dec 1st 2015 to Nov 30 2016, the basic income is provided to adults who have no income.
    # Before Dec 1st 2015, the basic income does not exist in the law, and calculating it returns its default value, which is 0.
    def formula_2015_12(person, period, parameters):
        age_condition = person('age', period) >= parameters(period).general.age_of_majority
        salary_condition = person('salary', period) == 0
        return age_condition * salary_condition * parameters(period).benefits.basic_income  # The '*' is also used as a vectorial 'and'. See http://openfisca.org/doc/coding-the-legislation/25_vectorial_computing.html#forbidden-operations-and-alternatives


class housing_allowance(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH
    label = "Housing allowange"
    reference = "https://law.gov.example/housing_allowance"  # Always use the most official source
    end = '2016-11-30'  # This allowance was removed on the 1st of Dec 2016. Calculating it before this date will always return the variable default value, 0.

    # This allowance was introduced on the 1st of Jan 1980. Calculating it before this date will always return the variable default value, 0.
    def formula_1980(household, period, parameters):
        return household('rent', period) * parameters(period).benefits.housing_allowance


# By default, you can use utf-8 characters in a variable. OpenFisca web API manages utf-8 encoding.
class pension(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Pension for the elderly. Pension attribuée aux personnes âgées."
    reference = [u"https://fr.wikipedia.org/wiki/Retraite_(économie)", u"https://ar.wikipedia.org/wiki/تقاعد"]

    def formula(person, period):
        '''
        A person's pension depends on its birth date.
        In french : La pension d'une personne est attribuée d'après la date de naissance.
        '''
        age_condition = person('age', period) >= parameters(period).general.age_of_retirement
        return age_condition
