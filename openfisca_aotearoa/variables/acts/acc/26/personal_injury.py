# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class acc_part_2__suffered_personal_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Has suffered a personal injury"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100910.html"

