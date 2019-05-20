# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Titled_Property, Person
from numpy import clip, floor


class rates_rebates__dependants(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Number of Persons classified as dependant for the purposes of Rates Rebates"


class rates_rebates__rates_total(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Total rates for the property"


class rates_rebates__combined_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    # Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    set_input = set_input_divide_by_period
    label = "Combined Income of applicant and others normally resident at property for the purposes of Rates Rebates"
    reference = "http://www.legislation.govt.nz/act/public/1973/0005/67.0/whole.html#DLM409685"


# Reference is accurate as at the time this formula was written,
# link to legislation is: http://www.legislation.govt.nz/act/public/1973/0005/67.0/DLM409673.html
class rates_rebates__rebate(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Yearly rebate applied to housing rates."
    reference = "Obtained from spreadsheet at Department Of Internal Affairs Innovation Lab"

    def formula(titled_properties, period, parameters):
        income_threshold = parameters(period).entitlements.rates_rebates.income_threshold
        additional_per_dependant = parameters(period).entitlements.rates_rebates.additional_per_dependant
        initial_contribution = parameters(period).entitlements.rates_rebates.initial_contribution
        maximum_allowable = parameters(period).entitlements.rates_rebates.maximum_allowable

        # sum allowable income including all the dependants for property
        allowable_income = (titled_properties.sum(titled_properties.members('rates_rebates__dependants', period)) * additional_per_dependant) + income_threshold

        # wrapping floor math function is non legislative and only to conform output of variable with existing infrastracture.
        excess_income = floor((titled_properties.sum(titled_properties.members('rates_rebates__combined_income', period)) - allowable_income) / 8).clip(min=0)

        # minus the initial contribution
        rates_minus_contribution = titled_properties('rates_rebates__rates_total', period) - initial_contribution

        # perform the calculation
        rebate = rates_minus_contribution - ((rates_minus_contribution / 3) + excess_income)

        # Ensures the results aren't negative (less than 0) or greater than the maximum_allowable
        return clip(rebate, 0, maximum_allowable)


class rates_rebates__maximum_income_for_full_rebate(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Maximum income eligible for the full rebate, less than this number should get full rebate"
    reference = "http://www.legislation.govt.nz/act/public/1973/0005/67.0/DLM409673.html"

    def formula(titled_properties, period, parameters):
        income_threshold = parameters(period).entitlements.rates_rebates.income_threshold
        additional_per_dependant = parameters(period).entitlements.rates_rebates.additional_per_dependant
        initial_contribution = parameters(period).entitlements.rates_rebates.initial_contribution

        # sum allowable income including all the dependants for property
        allowable_income = (titled_properties.sum(titled_properties.members('rates_rebates__dependants', period)) * additional_per_dependant) + income_threshold
        # what we're using to compute the maximum salary for full rebate
        rebate = parameters(period).entitlements.rates_rebates.maximum_allowable

        rates_total = titled_properties('rates_rebates__rates_total', period)

        return (((((rates_total - initial_contribution) - rebate) - ((rates_total - initial_contribution) / 3)) * 8) + allowable_income)


class rates_rebates__minimum_income_for_no_rebate(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Minimum income that returns no rebate. Less than this number gets a rebate"
    reference = "http://www.legislation.govt.nz/act/public/1973/0005/67.0/DLM409673.html"

    def formula(titled_properties, period, parameters):
        income_threshold = parameters(period).entitlements.rates_rebates.income_threshold
        additional_per_dependant = parameters(period).entitlements.rates_rebates.additional_per_dependant
        initial_contribution = parameters(period).entitlements.rates_rebates.initial_contribution

        # sum allowable income including all the dependants for property
        allowable_income = (titled_properties.sum(titled_properties.members('rates_rebates__dependants', period)) * additional_per_dependant) + income_threshold
        # what we're using to compute the maximum salary for full rebate
        rebate = 0

        rates_total = titled_properties('rates_rebates__rates_total', period)

        return (((((rates_total - initial_contribution) - rebate) - ((rates_total - initial_contribution) / 3)) * 8) + allowable_income)
