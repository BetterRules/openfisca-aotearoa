# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class total_benefits(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH
    label = "Sum of the benefits perceived by a household"
    reference = "https://stats.gov.example/benefits"

    def formula(household, period, parameters):
        basic_income_i = household.members('basic_income', period)  # Calculates the value of basic_income for each member of the household

        return (
            + household.sum(basic_income_i)  # Sum the household members basic incomes
            + household('housing_allowance', period)
            )


class total_taxes(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH
    label = "Sum of the taxes paid by a household"
    reference = "https://stats.gov.example/taxes"

    def formula(household, period, parameters):
        income_tax_i = household.members('income_tax', period)
        social_security_contribution_i = household.members('social_security_contribution', period)

        return (
            + household.sum(income_tax_i)
            + household.sum(social_security_contribution_i)
            + household('housing_tax', period.this_year) / 12
            )
