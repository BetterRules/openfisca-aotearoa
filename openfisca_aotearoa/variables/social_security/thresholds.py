# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class accommodation_supplement__below_income_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"income is below threshold?"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"


class accommodation_supplement__below_cash_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"cash is below threshold?"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"
