# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class social_security__is_in_full_employment(Variable):
    value_type = bool
    entity = Person
    default_value = False
    label = "Is in full employment or full-time employment"
    definition_period = MONTH
    reference = """
        full employment or full-time employment, in relation to any person, means
        (a) employment under a contract of service or apprenticeship which requires the person to work, whether on time or piece rates,
            no less than an average of 30 hours each week; or
        (b) self-employment of the person in any business, profession, trade, manufacture, or undertaking carried on for pecuniary profit
            for no less than an average of 30 hours each week; or
        (c) employment of the person for any number of hours which is regarded as full-time employment for the purposes of any award,
            agreement, or contract relating to that employment
        """
