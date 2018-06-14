# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class normally_lives_in_nz(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Normally lives in NZ"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"


class is_nz_resident(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Is NZ Resident"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"
