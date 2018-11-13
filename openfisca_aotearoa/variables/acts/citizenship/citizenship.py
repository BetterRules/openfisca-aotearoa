# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class citizenship__parent_born_in_nz_or_granted_citizenship_before_you_were_born
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__samoan_citizen
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__under_16_years_of_age
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__living_in_nz_for_at_least_240_days_in_each_year
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__living_in_nz_for_at_least_1350_days_over_5_years
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__intend_to_keep_living_in_nz
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__can_hold_basic_conversation_in_english
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__been_convicted_of_a_crime_in_last_3_years
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__spent_any_time_in_prison_in_the_last_7_years
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__ever_had_a_prison_sentence_of_more_than_5_years
    value_type = bool
    definition_period = MONTH
    label = u""
    reference = ""


class citizenship__eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Classified as eligible for NZ citizenship"
    reference = ""

    def formula(persons, period, parameters):
        return persons('is_resident', period) *\
          persons('citizenship__parent_born_in_nz_or_granted_citizenship_before_you_were_born', period)
