# -*- coding: utf-8 -*-

from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import Variable, MONTH, ETERNITY, set_input_dispatch_by_period


class social_security__meets_residential_requirements_for_certain_benefits(Variable):
    value_type = bool
    entity = Person
    label = u"Residential requirements for certain benefits"
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM363796.html"

    def formula(persons, period, parameters):
        # (a) is a New Zealand citizen, or is a person who holds a residence
        # class visa under the Immigration Act 2009
        is_citizen_or_resident = persons('is_citizen_or_resident', period)

        # (b) is ordinarily resident in New Zealand when he or she first
        # applies for the benefit; and
        ordinarily_lives_in_nz = persons(
            'social_security__is_ordinarily_resident_in_new_zealand', period)

        # (c) except in the case of a person who is recognised as a refugee or
        #     a protected person in New Zealand under
        #     the Immigration Act 2009, has resided continuously in New Zealand
        #     for a period of at least 2 years at any one time,
        is_refugee_or_protected = \
            persons('immigration__is_recognised_refugee', period) \
            + persons('immigration__is_protected_person', period)

        enough_years_in_nz = persons(
            'social_security__has_resided_continuously_in_nz_for_a_period_of_at_least_2_years_at_any_one_time',
            period)

        return (is_citizen_or_resident * ordinarily_lives_in_nz) \
            + (is_refugee_or_protected * enough_years_in_nz)


class social_security__is_ordinarily_resident_in_new_zealand(Variable):
    value_type = bool
    entity = Person
    label = u"is ordinarily resident in New Zealand"
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM363772.html"


class social_security__has_resided_continuously_in_nz_for_a_period_of_at_least_2_years_at_any_one_time(Variable):
    value_type = bool
    entity = Person
    label = u"has resided continuously in New Zealand for a period of at least 2 years at any one time"
    definition_period = ETERNITY
