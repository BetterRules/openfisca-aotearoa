# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class acc__elected_for_weekly_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Person eligible and elected to receive weekly compensation instead of superannuation"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM105440.html#DLM105440"


class acc__is_receiving_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is receiving compensation payment through ACC"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM105404.html#DLM105404"
