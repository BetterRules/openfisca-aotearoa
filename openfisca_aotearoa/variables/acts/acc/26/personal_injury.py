# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__part_2__suffered_personal_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Has suffered a personal injury"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100910.html"
