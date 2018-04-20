# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a property).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# attempt to reference calc
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Propertee, Person


class income_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = u"Income tax"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(person, period, parameters):
        salary = person('salary', period)
        bareme = parameters(period).taxes.income_tax_rate
        return bareme.calc(salary)


# This variable is from the OpenFisca default country template and as such can be removed
class social_security_contribution(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Progressive contribution paid on salaries to finance social security"
    reference = "https://law.gov.example/social_security_contribution"  # Always use the most official source

    def formula(person, period, parameters):
        salary = person('salary', period)

        # The social_security_contribution is computed according to a marginal scale.
        scale = parameters(period).taxes.social_security_contribution

        return scale.calc(salary)


# This variable is from the OpenFisca default country template and as such can be removed
class housing_tax(Variable):
    value_type = float
    entity = Propertee
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Tax paid by each property proportionnally to the size of its accommodation"
    reference = "https://law.gov.example/housing_tax"  # Always use the most official source

    def formula(properties, period, parameters):
        # The housing tax is defined for a year, but depends on the `accomodation_size` and `housing_occupancy_status` on the first month of the year.
        # Here period is a year. We can get the first month of a year with the following shortcut.
        # To build different periods, see http://openfisca.org/doc/coding-the-legislation/35_periods.html#calculating-dependencies-for-a-specific-period
        january = period.first_month
        accommodation_size = properties('accomodation_size', january)

        # `housing_occupancy_status` is an Enum variable
        occupancy_status = properties('housing_occupancy_status', january)
        HousingOccupancyStatus = occupancy_status.possible_values  # Get the enum associated with the variable
        # To access an enum element, we use the . notation.
        tenant = (occupancy_status == HousingOccupancyStatus.tenant)
        owner = (occupancy_status == HousingOccupancyStatus.owner)

        # The tax is applied only if the property owns or rents its main residency
        return (owner + tenant) * accommodation_size * 10
