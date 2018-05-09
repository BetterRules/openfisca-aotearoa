# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a property).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Propertee, Person
from numpy import clip


# This is a 'temporary' variable used specifically for the rates rebates
# Due to the structure not yet being clear, this may need to be moved, renamed.
class dependants(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Number of Persons classified as dependant on the entity Person for the purposes of rates rebates"


class rates(Variable):
    value_type = float
    entity = Propertee
    definition_period = YEAR


class rates_rebate(Variable):
    value_type = float
    entity = Propertee
    definition_period = YEAR
    label = "Yearly rebate applied to housing rates. Defined on a calendar year, not a fiscal year."
    reference = ""

    def formula(properties, period, parameters):
        income_threshold = parameters(period).benefits.rates_rebates.income_threshold
        additional_per_dependant = parameters(period).benefits.rates_rebates.additional_per_dependant
        initial_contribution = parameters(period).benefits.rates_rebates.initial_contribution
        maximum_allowable = parameters(period).benefits.rates_rebates.maximum_allowable

        # sum allowable income including all the dependants for property
        allowable_income = (properties.sum(properties.members('dependants', period)) * additional_per_dependant) + income_threshold

        # calculate the excess income based on the allowable income
        excess_income = (properties.sum(properties.members('salary', period)) - allowable_income) / 8

        # minus the initial contribution
        rates_minus_contribution = properties('rates', period) - initial_contribution

        # perform the calculation
        rebate = rates_minus_contribution - ((rates_minus_contribution / 3) + excess_income)

        # clips the results between 0 and the maximum_allowable
        return clip(rebate, 0, maximum_allowable)


class maximum_income_for_full_rebate(Variable):
    value_type = float
    entity = Propertee
    definition_period = YEAR
    label = "Maximum income eligible for the full rebate, less than this number should get full rebate"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(properties, period, parameters):
        ratesperiod = period.offset(-6, 'month')
        income_threshold = parameters(ratesperiod).benefits.rates_rebates.income_threshold
        additional_per_dependant = parameters(ratesperiod).benefits.rates_rebates.additional_per_dependant
        initial_contribution = parameters(ratesperiod).benefits.rates_rebates.initial_contribution

        # sum allowable income including all the dependants for property
        allowable_income = (properties.sum(properties.members('dependants', ratesperiod)) * additional_per_dependant) + income_threshold
        # what we're using to compute the maximum salary for full rebate
        rebate = parameters(period).benefits.rates_rebates.maximum_allowable

        return (((((properties('rates', period) - initial_contribution) - rebate) - ((properties('rates', period) - initial_contribution) / 3)) * 8) + allowable_income)


class minimum_income_for_no_rebate(Variable):
    value_type = float
    entity = Propertee
    definition_period = YEAR
    label = "Minimum income that returns no rebate. Less than this number gets a rebate"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(properties, period, parameters):
        ratesperiod = period.offset(-6, 'month')
        income_threshold = parameters(ratesperiod).benefits.rates_rebates.income_threshold
        additional_per_dependant = parameters(ratesperiod).benefits.rates_rebates.additional_per_dependant
        initial_contribution = parameters(ratesperiod).benefits.rates_rebates.initial_contribution

        # sum allowable income including all the dependants for property
        allowable_income = (properties.sum(properties.members('dependants', ratesperiod)) * additional_per_dependant) + income_threshold
        # what we're using to compute the maximum salary for full rebate
        rebate = 0

        return (((((properties('rates', period) - initial_contribution) - rebate) - ((properties('rates', period) - initial_contribution) / 3)) * 8) + allowable_income)
