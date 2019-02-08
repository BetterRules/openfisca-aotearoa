# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class super___eligibility_age(Variable):
    value_type = int
    entity = Person
    definition_period = ETERNITY
    label = u"The age the applicant will be eligible for NZ Super."
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/DLM114223.html"

    def formula(persons, period, parameters):
        return persons('super__eligibility', period) * parameters(period).entitlements.superannuation.age_qualification


class super__eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Classified as eligible for NZ Super"
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/DLM113987.html"

    def formula(persons, period, parameters):
        return persons('is_citizen_or_resident', period) *\
            not_((persons('total_number_of_years_lived_in_nz_since_age_20', period) < 10)) *\
            not_((persons('total_number_of_years_lived_in_nz_since_age_50', period) < 5)) *\
            not_(persons('acc__is_receiving_compensation', period)) +\
            persons(
                'veterans_support__is_entitled_to_be_paid_veterans_pension', period)


class super__is_being_paid_nz_superannuation(Variable):
    value_type = bool
    entity = Person
    label = "New Zealand superannuation"
    definition_period = MONTH
