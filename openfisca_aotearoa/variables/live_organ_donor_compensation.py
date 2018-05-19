# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Titled_Property, Person
from numpy import clip, floor

class weekly_compensation_before_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR # TODO - determine whether we need to get WEEK to work
    label = u"The amount payable as compensation per week before tax"

    def formula(persons, period, parameters):
        # income_threshold = parameters(period).benefits.rates_rebates.income_threshold
        # additional_per_dependant = parameters(period).benefits.rates_rebates.additional_per_dependant
        # initial_contribution = parameters(period).benefits.rates_rebates.initial_contribution
        # maximum_allowable = parameters(period).benefits.rates_rebates.maximum_allowable
        # maximum_allowable = 10000000.00

        # # sum allowable income including all the dependants for property
        # allowable_income = (titled_properties.sum(titled_properties.members('dependants_as_per_rates_rebates', period)) * additional_per_dependant) + income_threshold

        # # wrapping floor math function is non legislative and only to conform output of variable with existing infrastracture.
        # excess_income = floor((titled_properties.sum(titled_properties.members('combined_income_as_per_rates_rebates', period)) - allowable_income) / 8)

        # # minus the initial contribution
        # rates_minus_contribution = titled_properties('rates_total_as_per_rates_rebates', period) - initial_contribution

        # # perform the calculation
        # rebate = rates_minus_contribution - ((rates_minus_contribution / 3) + excess_income)

        # # Ensures the results aren't negative (less than 0) or greater than the maximum_allowable
        return persons('salary_per_pay', period)
        # return clip(1200.00, 0, 10000000)

class PayFrequency(Enum):
    weekly = u'Weekly'
    fortnightly = u'Fortnightly'
    four_weekly = u'Four Weekly'
    monthly = u'Monthly'

class pay_frequency(Variable):
    value_type = Enum
    possible_values = PayFrequency
    default_value = PayFrequency.weekly  # The default is mandatory
    entity = Person
    definition_period = YEAR
    label = u"The frequency at which a person is paid"

class salary_per_pay(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR # TODO - determine whether we need to get WEEK to work
    label = u"The salary earned by a person before tax"

class kiwisaver_member(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Whether the person currently pays into Kiwisaver"
    definition_period = YEAR