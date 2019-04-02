# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__the_corporation_exercised_descretion_for_attendant_care_as_per_section_68_3(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101402.html"

class acc__the_corporation_exercised_descretion_for_child_care_as_per_section_68_3(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101402.html"