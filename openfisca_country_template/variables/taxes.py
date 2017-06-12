# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See https://doc.openfisca.fr/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class income_tax(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = u"Income tax"
    url = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(person, period, legislation):
        return person('salary', period) * legislation(period).taxes.income_tax_rate


class social_security_contribution(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = u"Progressive contribution paid on salaries to finance social security"
    url = "https://law.gov.example/social_security_contribution"  # Always use the most official source

    def formula(person, period, legislation):
        salary = person('salary', period)

        # The social_security_contribution is computed according to a marginal scale.
        scale = legislation(period).taxes.social_security_contribution

        return scale.calc(salary)


class housing_tax(Variable):
    column = FloatCol
    entity = Household
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Tax paid by each household proportionnally to the size of its accommodation"
    url = "https://law.gov.example/housing_tax"  # Always use the most official source

    def formula(household, period, legislation):
        # The housing tax is defined for a year, but depends on the `accomodation_size` on the first month of the year.
        # Here period is a year. We can get the first month of a year with the following shortcut.
        # To build different periods, see https://doc.openfisca.fr/coding-the-legislation/35_periods.html#calculating-dependencies-for-a-specific-period
        january = period.first_month
        return household('accomodation_size', january) * 10
