# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__the_corporation_exercised_descretion_as_per_section_68_3(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH