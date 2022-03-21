# -*- coding: utf-8 -*-

from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import MONTH, Variable


class social_security__eligible_for_accommodation_supplement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Accommodation Supplement"

    reference = """
        61DH Purpose of accommodation supplement

        The purpose of sections 61E to 61EC and Schedule 18 is to provide targeted
        financial assistance to help certain people with high accommodation costs
        to meet those costs.
        """

    def formula(persons, period, parameters):
        # Based on MSD's web page
        # https://www.workandincome.govt.nz/products/a-z-benefits/accommodation-supplement.html
        age_threshold = parameters(
            period).entitlements.social_security.accommodation_supplement.age_threshold
        # NOTE: using the age at the start of the month
        # Age changes on a DAY, but this calculation only has a granularity of MONTH
        age_requirement = persons("age", period.start) >= age_threshold

        """
        http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM363772.html
        Notwithstanding anything to the contrary in this Act or Part 6 of the Veterans’
        Support Act 2014 or the New Zealand Superannuation and Retirement Income Act 2001,
        the chief executive may, in the chief executive’s discretion, refuse to grant any
        benefit or may terminate or reduce any benefit already granted or may grant a
        benefit at a reduced rate in any case where the chief executive is satisfied
        (a) that the applicant, or the spouse or partner of the applicant or any person
        in respect of whom the benefit or any part of the benefit is or would be payable,
        is not ordinarily resident in New Zealand; """
        in_nz = persons(
            'social_security__is_ordinarily_resident_in_new_zealand', period)
        resident_or_citizen = persons('is_resident', period) + persons(
            'is_permanent_resident', period) + persons('is_nz_citizen', period)
        social_security__has_accomodation_costs = persons(
            'social_security__has_accomodation_costs', period)
        not_social_housing = (
            persons('eligible_for_social_housing', period) == 0)

        income = persons(
            'accommodation_supplement__below_income_threshold', period)
        cash = persons(
            'accommodation_supplement__below_cash_threshold', period)

        return age_requirement * resident_or_citizen * in_nz * social_security__has_accomodation_costs * not_social_housing * income * cash


class eligible_for_social_housing(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Has social housing?"
    definition_period = MONTH
    reference = "Social Security Act 1964 - 61EA Accommodation supplement http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM362856"
