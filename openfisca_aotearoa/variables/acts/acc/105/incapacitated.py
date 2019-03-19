# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class incapacity_for_employment__corporation_determination(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = u"Corporation determination of incapacity"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101462.html"


class incapacity_for_employment__by_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = u"The incapacity is caused by the injury for which they have cover"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101462.html"
