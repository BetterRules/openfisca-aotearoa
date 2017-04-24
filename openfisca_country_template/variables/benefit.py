# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class basic_income(DatedVariable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = "Basic income provided to adults"
    url = "https://law.gov.example/basic_income"  # Always use the most official source

    # Since Dec 1st 2016, the basic income is provided to any adult, without cousidering their income.
    @dated_function(start = date(2016, 12, 1))
    def function_from_2016_12(person, period, legislation):
        age_condition = person('age', period) >= legislation(period).age_of_majority
        return age_condition * legislation(period).basic_income  # This '*' is a vectorial 'if'. See https://doc.openfisca.fr/coding-the-legislation/30_case_disjunction.html#simple-multiplication

    # From Dec 1st 2015 to Nov 30 2016, the basic income is provided to adults who have no income.
    # Before Dec 1st 2015, the basic income does not exist in the law, and calculating it returns its default value, which is 0.
    @dated_function(start = date(2015, 12, 1), stop = date(2016, 11, 30))
    def function_until_2016_12(person, period, legislation):
        age_condition = person('age', period) >= legislation(period).age_of_majority
        salary_condition = person('salary', period) == 0
        return age_condition * salary_condition * legislation(period).basic_income  # The '*' is also used as a vectorial 'and'. See https://doc.openfisca.fr/coding-the-legislation/25_vectorial_computing.html#forbidden-operations-and-alternatives
