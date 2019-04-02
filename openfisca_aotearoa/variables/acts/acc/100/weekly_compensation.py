# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class weekly_compensation__lodges_a_claim(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"A claimant who has cover and who lodges a claim for weekly compensation"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100910.html"
