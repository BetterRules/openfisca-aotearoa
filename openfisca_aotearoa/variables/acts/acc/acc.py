# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__is_receiving_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is receiving compensation payment through ACC"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM105404.html#DLM105404"
