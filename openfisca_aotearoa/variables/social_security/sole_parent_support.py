from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *

"""
MSD Policy (retrieved August 2018 from )
    https://www.workandincome.govt.nz/products/a-z-benefits/sole-parent-support.html

You may get Sole Parent Support if you are:

    * aged 20 or older
    * a single parent or caregiver with one or more dependent children under 14
    * not in a relationship
    * without adequate financial support
    * a New Zealand citizen or permanent resident who has been here for at least two years
    at any one time since becoming a citizen or permanent resident, and who normally lives here.
"""


class social_security__eligible_for_sole_parent_support(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Job Seeker Support"

    def formula(persons, period, parameters):
        # The applicant
        in_nz = persons('normally_lives_in_nz', period)
        resident_or_citizen = \
            persons('is_resident', period) + \
            persons('is_permanent_resident', period) + \
            persons('is_nz_citizen', period)

        years_in_nz = persons('sole_parent_support__meets_years_in_nz_requirement', period)
        age_requirement = persons('sole_parent_support__meets_age_threshold', period)

        # TODO: There is only one parent
        # TODO isInadequatelySupportedByPartner
        # TODO isMaintainingChild

        # income low enough?
        income = persons('sole_parent_support__below_income_threshold', period)

        return in_nz * resident_or_citizen * \
            age_requirement * income * years_in_nz


class sole_parent_support__meets_age_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the age test for sole parent support?"
    definition_period = MONTH
    reference = "TODO"

    def formula(persons, period, parameters):
        # old enough?
        age_threshold = parameters(period).entitlements.social_security.sole_parent_support.age_threshold
        return persons("age", period) >= age_threshold


class sole_parent_support__meets_years_in_nz_requirement(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the sole parent support test for number of continuous years lived in nz"
    definition_period = MONTH
    reference = "TODO"

    def formula(persons, period, parameters):
        # been in NZ log enough?
        min_years = parameters(period).entitlements.social_security.sole_parent_support.minumum_continuous_time_in_nz
        years_in_nz = persons('number_of_years_lived_in_nz', period)
        return years_in_nz >= min_years
