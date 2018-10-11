# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class super__living_alone(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Is a person considered as living alone"
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/whole.html#DLM5578822"


class super__has_partner_in_long_term_care_or_rest_home(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Has a partner in long term care or rest home"
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/DLM114223.html"


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
            (persons('age', period) >= 65) *\
            not_(persons('acc__is_receiving_compensation', period)) +\
            persons('veterans_support__is_entitled_to_be_paid_veterans_pension', period)
