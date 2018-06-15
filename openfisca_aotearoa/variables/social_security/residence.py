# -*- coding: utf-8 -*-

from openfisca_core.model_api import Variable, ETERNITY
from openfisca_aotearoa.entities import Person


class normally_lives_in_nz(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Person normally lives in New Zealand. (Is ordinarily resident in New Zealand when he or she first applies for the benefit)"
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM363796"
