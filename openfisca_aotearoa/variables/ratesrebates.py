# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a property).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import _Property
from numpy import array


# This is a 'temporary' variable used specifically for the rates rebates
# Due to the structure not yet being clear, this may need to be moved, renamed.
class dependants(Variable):
    value_type = int
    entity = _Property
    definition_period = YEAR
    label = u"Number of Persons classified as dependant on the entity Person for the purposes of rates rebates"


class rates(Variable):
    value_type = float
    entity = _Property
    definition_period = YEAR


class income(Variable):
    value_type = float
    entity = _Property
    definition_period = YEAR
    label = "Combined income of Property persons"
    reference = ""  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(_property, period, parameters):
        salary = _property.members('salary', period)
        return _property.sum(salary)


class rates_rebate(Variable):
    value_type = float
    entity = _Property
    definition_period = YEAR
    label = "Actual amount available to the person at the end of the month"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(_property, period, parameters):
        allowable_income = parameters(period).benefits.rates_rebates.income_threshold
        + (_property('dependants', period) * parameters(period).benefits.rates_rebates.additional_per_dependant)
        
        excess_income = (_property('income', period) - allowable_income) / 8
        ratesminuscontribution = _property('rates', period) - parameters(period).benefits.rates_rebates.initial_contribution
        ratesandexcess = (ratesminuscontribution / 3) + excess_income
        rebate = ratesminuscontribution - ratesandexcess

        if rebate < 0:
            rebate = array([0])
        elif rebate > parameters(period).benefits.rates_rebates.maximum_allowable:
            rebate = array([parameters(period).benefits.rates_rebates.maximum_allowable])

        return rebate

