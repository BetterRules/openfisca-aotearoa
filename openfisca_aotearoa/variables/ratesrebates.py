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
    label = "Actual amount available to the person at the end of the month"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(properties, period, parameters):
        income_threshold = parameters(period).benefits.rates_rebates.income_threshold
        additional_per_dependant = parameters(period).benefits.rates_rebates.additional_per_dependant
        initial_contribution = parameters(period).benefits.rates_rebates.initial_contribution
        maximum_allowable = parameters(period).benefits.rates_rebates.maximum_allowable

        # sum all the dependants for property first
        allowable_income = (properties.sum(properties.members('dependants', period)) * additional_per_dependant) + income_threshold
        
        # sum all properties members first
        excess_income = (properties.sum(properties.members('salary', period)) - allowable_income) / 8

        ratesminuscontribution = properties('rates', period) - initial_contribution

        ratesandexcess = (ratesminuscontribution / 3) + excess_income

        rebate = ratesminuscontribution - ratesandexcess

        return clip(rebate, 0, maximum_allowable)


