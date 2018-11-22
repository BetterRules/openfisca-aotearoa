# -*- coding: utf-8 -*-

from openfisca_core.model_api import Variable
from openfisca_core.periods import MONTH, DAY, YEAR, ETERNITY
from openfisca_aotearoa.entities import Person


class citizenship__citizenship_by_grant_may_be_authorized(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"

    def formula_2005_04_20(persons, period, parameters):
        return persons('age', period) >= parameters(period).citizenship.by_grant.minimum_age_threshold * \
            persons('is_of_full_capacity', period) * \
            persons('citizenship__meets_minimum_presence_requirements', period) * \
            persons('citizenship__is_of_good_character', period) * \
            persons('citizenship__has_sufficient_knowledge_of_the_responsibilities_and_privileges_attaching_to_nz_citizenship') * \
            persons('citizenship__has_sufficient_knowledge_of_the_english_language', period) * \
            (persons('citizenship__intends_to_reside_in_nz', period) + persons('citizenship__intends_to_enter_or_continue_crown_service', period))


class citizenship__meets_minimum_presence_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = u"Applicant was present in New Zealand for a min of 1,350 days during the 5 years immediately preceding the date of application"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"

    def formula(persons, period, parameters):
        # that the applicant was present in New Zealand—
        # (i) for a minimum of 1350 days during the 5 years immediately preceding the date of the application; and
        # persons('immigration__entitled_to_stay_indefinitely', period) * \
        # (ii) for at least 240 days in each of those 5 years,—
        # being days during which the applicant was entitled in terms of the Immigration Act 2009 to be in New Zealand indefinitely
        return persons('number_of_days_present_in_nz_in_preceeding_12_month') > parameters(period).citizenship.by_grant.minimum_days_present_in_preceeding_5_years


class number_of_days_present_in_nz_in_preceeding_12_month(Variable):
    value_type = int
    entity = Person
    definition_period = DAY
    label = u"Number of days present in NZ in last 12 months"
    unit = 'years'
    default_value = -9999
    # A person's age is computed according to their birth date.

    # def formula(persons, period, parameters):
    #     return persons


class present_in_new_zealand(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Applicant was present in New Zealand on this day"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class immigration__holds_indefinite_stay_visa(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "is entitled in terms of the Immigration Act 2009 to be in New Zealand indefinitely"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__is_of_good_character(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "applicant is of good character"
    reference = ["http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html", "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443872.html"]


class citizenship__has_sufficient_knowledge_of_the_responsibilities_and_privileges_attaching_to_nz_citizenship(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "applicant has sufficient knowledge of the English language"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__has_sufficient_knowledge_of_the_english_language(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "has sufficient knowledge of the English language"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__intends_to_reside_in_nz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "intends to continue to reside in New Zealand"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__intends_to_enter_or_continue_crown_service(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "intends to enter into or continue in Crown service under the New Zealand Government, or service under an international organisation of which the New Zealand Government is a member, or service in the employment of a person, company, society, or other body of persons resident or established in New Zealand"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"
