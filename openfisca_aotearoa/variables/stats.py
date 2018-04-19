# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a property).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import _Property


class total_benefits(Variable):
    value_type = float
    entity = _Property
    definition_period = MONTH
    label = "Sum of the benefits perceived by a Property"
    reference = "https://stats.gov.example/benefits"

    def formula(_property, period, parameters):
        basic_income_i = _property.members('basic_income', period)  # Calculates the value of basic_income for each member of the property

        return (
            + _property.sum(basic_income_i)  # Sum the property members basic incomes
            + _property('housing_allowance', period)
            )


class total_taxes(Variable):
    value_type = float
    entity = _Property
    definition_period = MONTH
    label = "Sum of the taxes paid by a property"
    reference = "https://stats.gov.example/taxes"

    def formula(_property, period, parameters):
        income_tax_i = _property.members('income_tax', period)
        social_security_contribution_i = _property.members('social_security_contribution', period)

        return (
            + _property.sum(income_tax_i)
            + _property.sum(social_security_contribution_i)
            + _property('housing_tax', period.this_year) / 12
            )
