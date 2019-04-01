# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__the_corporation_decides_to_provide_or_contribute_to_attendant_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH

