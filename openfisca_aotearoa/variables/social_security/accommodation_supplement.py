from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *


class social_security__eligible_for_accommodation_supplement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Accommodation Supplement"

    """
        age => 16
        normally_lives_in_nz: True
        is_resident: True
        has_accomodation_costs: True
        has_social_housing: False
        income_below_threshold_for_accommodation_supplement: True
        cash_below_threshold_for_accommodation_supplement: True
    """
    def formula(persons, period, parameters):
        # Based on MSD's web page
        # https://www.workandincome.govt.nz/products/a-z-benefits/accommodation-supplement.html
        age_threshold = parameters(period).entitlements.social_security.accommodation_supplement.age_threshold

        age_requirement = persons("age", period) >= age_threshold

        in_nz = persons('normally_lives_in_nz', period)

        resident_or_citizen = persons('is_resident', period) + persons('is_permanent_resident', period) + persons('is_nz_citizen', period)
        has_accomodation_costs = persons('has_accomodation_costs', period)
        does_not_have_social_housing = (persons('has_social_housing', period) == 0)

        income = persons('income_below_threshold_for_accommodation_supplement', period)
        cash = persons('cash_below_threshold_for_accommodation_supplement', period)

        return age_requirement * resident_or_citizen * in_nz * has_accomodation_costs * does_not_have_social_housing * income * cash


class income_below_threshold_for_accommodation_supplement(Variable):
    value_type = bool
    entity = Person
    label = u"Income is below threshold"
    definition_period = MONTH


class cash_below_threshold_for_accommodation_supplement(Variable):
    value_type = bool
    entity = Person
    label = u"Cash is below threshold"
    definition_period = MONTH


class has_accomodation_costs(Variable):
    value_type = bool
    entity = Person
    label = u"Has accommodation costs"
    definition_period = MONTH


class has_social_housing(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Has social housing?"
    definition_period = MONTH
