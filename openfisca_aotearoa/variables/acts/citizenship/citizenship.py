# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class citizenship__present_for_min_1350_days_during_5_years(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Applicant was present in New Zealand for a min of 1,350 days during the 5 years immediately preceding the date of application"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__present_for_at_least_240_days_in_each_of_those_5_years(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Applicant was present in New Zealand for at least 240 days in each of those 5 years"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__eligibility(Variable):
    value_type = bool
    entity = Person
    entity = Person
    definition_period = MONTH
    label = u"Classified as eligible for NZ citizenship"

    def formula(persons, period, parameters):
        return persons('citizenship__present_for_min_1350_days_during_5_years', period) *\
            persons('citizenship__present_for_at_least_240_days_in_each_of_those_5_years', period)
