from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *


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
        age_threshold = parameters(period).entitlements.social_security.accommodation_supplement.age_threshold

        age_requirement = persons("age", period) >= age_threshold

        in_nz = persons('normally_lives_in_nz', period)

        resident_or_citizen = persons('is_resident', period) + persons('is_permanent_resident', period) + persons('is_nz_citizen', period)
        social_security__has_accomodation_costs = persons('social_security__has_accomodation_costs', period)
        not_social_housing = (persons('eligible_for_social_housing', period) == 0)

        income = persons('accommodation_supplement__below_income_threshold', period)
        cash = persons('accommodation_supplement__below_cash_threshold', period)

        return age_requirement * resident_or_citizen * in_nz * social_security__has_accomodation_costs * not_social_housing * income * cash


class eligible_for_social_housing(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Has social housing?"
    definition_period = MONTH
    reference = "Social Security Act 1964 - 61EA Accommodation supplement http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM362856"
