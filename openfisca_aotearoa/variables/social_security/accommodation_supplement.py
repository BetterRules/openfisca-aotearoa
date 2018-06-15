from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *


class social_security__eligible_for_accommodation_supplement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Accommodation Supplement"
    reference = "TODO"

    """
        age => 16
        normally_lives_in_nz: True
        is_nz_resident: True
        has_accomodation_costs: True
        has_social_housing: False
        accommodation_supplement__below_income_threshold: True
        accommodation_supplement__below_cash_threshold: True
    """
    def formula(persons, period, parameters):
        age_threshold = parameters(period).entitlements.social_security.accommodation_supplement.age_threshold
        age_requirement = persons("age", period) >= age_threshold
        nzlandie = persons('normally_lives_in_nz', period) * persons('is_nz_resident', period)
        has_accomodation_costs = persons('has_accomodation_costs', period)
        return age_requirement * nzlandie * has_accomodation_costs


class has_accomodation_costs(Variable):
    value_type = bool
    # default_value = True
    entity = Person
    label = u"Has accommodation costs"
    definition_period = MONTH  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"


class has_social_housing(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Has social housing?"
    definition_period = MONTH  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"
