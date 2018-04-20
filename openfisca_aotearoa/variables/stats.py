# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a property).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Propertee


class total_benefits(Variable):
    value_type = float
    entity = Propertee
    definition_period = MONTH
    label = "Sum of the benefits perceived by a Property"
    reference = "https://stats.gov.example/benefits"

    def formula(properties, period, parameters):
        basic_income_i = properties.members('basic_income', period)  # Calculates the value of basic_income for each member of the property

        return (
            + properties.sum(basic_income_i)  # Sum the property members basic incomes
            + properties('housing_allowance', period)
            )


class total_taxes(Variable):
    value_type = float
    entity = Propertee
    definition_period = MONTH
    label = "Sum of the taxes paid by a property"
    reference = "https://stats.gov.example/taxes"

    def formula(properties, period, parameters):
        income_tax_i = properties.members('income_tax', period)
        social_security_contribution_i = properties.members('social_security_contribution', period)

        return (
            + properties.sum(income_tax_i)
            + properties.sum(social_security_contribution_i)
            + properties('housing_tax', period.this_year) / 12
            )

# This file is from the OpenFisca default country template and as such can be removed
